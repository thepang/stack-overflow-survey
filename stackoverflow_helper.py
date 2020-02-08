import pandas as pd
import dictionaries as d

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, roc_curve
from sklearn.model_selection import cross_val_score

def remove_unneeded_data(data):
    """
    There are rows that need to be removed from the data set.
    They are mainly related to unemployed or rows that are unfit for analysis.
    """
    
    # We are interested in the population that reports as being employed
    # and considers developing a major part of their profession.
    data = data[(data['MainBranch']=='I am a developer by profession') & (data['Employment']=='Employed full-time')]
    
    # We cannot train on rows that do not have a value for our target feature so they are removed.
    data = data[data['JobSat'].notnull()]

    return data
    

def replace_data(data, mapping_dictionary, additional_data=None):
    """
    Returns a new dataframe with columns that correspond to the keys in mapping_dctionary.
    All the values in the columns are updated using the values in mapping_dictionary.
    If additional_data is set (a list of column names), the columns are added without updating values.
    """

    new_df = pd.DataFrame()
    
    for column in mapping_dictionary.keys():
        new_df[column] = data[column]

    new_df = new_df.replace(mapping_dictionary) 
    
    if additional_data != None:
        for column in additional_data:
            new_df[column] = data[column]
    
    return new_df


def fill_nans(data):
    """
    Returns dataframe with NaNs filled with mean or mode, 
    based on some hard coded understanding of the data.
    """
    
    
    for column in data.columns:
        if column in ['YearsCode', 'Age1stCode', 'YearsCodePro']:
            data[column] = data[column].fillna(data[column].dropna().astype('int64').mean())
        elif column in ['Age', 'ConvertedComp', 'WorkWeekHrs', 'CodeRevHrs', 'OrgSize', 'SOPartFreq', '']:
            data[column] = data[column].fillna(data[column].mean())
        else:
            new_mode = data[column].mode()
            data[column] = data[column].fillna(new_mode[0])
    return data

def multiselect_parser(df, column):
    """
    Iterates through the dataframe and splits the text in 'column'.
    Returns a dictionary where the key is the row's index. 
    Value is another dictionary where:
        Key is the substring of text in column (split on ';')
        Value is 1.
    """
    d = {}
    for index, row in df.iterrows():
        not_strings = []
        if type(row[column]) == str:
            list_ = row[column].split(';')
        else:
            list_ = []
        items = {}
        
        for item in list_:
            items[f'{column}_{item}'] = 1
        
        d[index] = items

    return d


def get_analysis_data(raw_data, columns_no_replace=None):
    """
    Returns the new dataframe. New dataframe's columns correspond to keys in survey_values.
    Optional value: Pass in column names that do not need replacement.
    """
    
    ###### 1. Remove unneeded rows
    culled = remove_unneeded_data(raw_data)
    
    ###### 2. Replace text values with numbers for ordinal/boolean questions
    mapped = replace_data(culled, d.survey_values, columns_no_replace)

    ###### 3. Custom logic for certain fields
    # WorkWeekHrs has numbers larger than 168 (total number of hours available on a week). 
    # Reducing all over 100 to 100.
    if 'WorkWeekHrs' in mapped.columns:
        mapped.loc[mapped['WorkWeekHrs'] > 100, 'WorkWeekHrs'] = 100
    
    # Regionalize country data
    if 'Country' in mapped.columns:
        countries = raw_data['Country'].replace(d.country_to_region)
        mapped = mapped.merge(pd.get_dummies(countries), on='Respondent')
        mapped = mapped.drop(columns = ['Country'])
        
    # Parse columns with multivalues into dummy variables
    for column in mapped.columns:
        if column in d.multi_select_fields:
            dy = multiselect_parser(mapped, column)
            dy = pd.DataFrame(dy).T.fillna(0)
            mapped = mapped.merge(pd.get_dummies(dy), left_on='Respondent', right_index=True)
            mapped = mapped.drop(columns = column)
    
    # Add dummied data for the following columns
    for column in mapped.columns:
        if column in ['UndergradMajor', 'OpSys', 'ITperson', 'OffOn', 'SocialMedia', 'ScreenName']:
            mapped = mapped.merge(pd.get_dummies(mapped[column]), on='Respondent')
            mapped = mapped.drop(columns = column)
        
    ###### 4. Fill the nans (custom logic in fill_nans function)
    to_return = fill_nans(mapped)

    return to_return



## Post import feature engineering

def test_model(train_input, train_output, test_input, test_expected, n=35, md=7, msl=23, c='entropy'):
    """
    Runs RandomForest Classifier on train_input and train_output using the default values: 
    n_estimators=3, max_depth=7, min_samples_leaf=23, criterion='entropy'.
    Returns a dictionary of scores where the keys are 'roc_auc', 'accuracy', 'precision', and 'recall'.
    """
    rfc = RandomForestClassifier(n_estimators=n, max_depth=md, min_samples_leaf=msl, criterion=c)
    rfc.fit(train_input, train_output)

    accuracy = cross_val_score(rfc, test_input, test_expected, cv=5, scoring='accuracy')
    precision = cross_val_score(rfc, test_input, test_expected, cv=5, scoring='precision')
    recall = cross_val_score(rfc, test_input, test_expected, cv=5, scoring='recall')
    f1 = cross_val_score(rfc, test_input, test_expected, cv=5, scoring='f1')
    roc_auc_score = cross_val_score(rfc, test_input, test_expected, cv=5, scoring='roc_auc')

    results = {}

    for name, item in [('roc_auc', roc_auc_score), 
                       ('accuracy', accuracy), 
                       ('precision', precision), 
                       ('recall', recall), ('f1', f1)]:
        results.update({name: item.mean()})
    return results

def get_sum_of_tech(data):
    """
    Just sums the 1s from any column with text "DesireNextYear"
    with the assumption that general larger desire to work with tech correlates with higher JobSat.

    Does the same for those that respondant said they worked with it, just 'cause.
    """
    d = {}
    for index, row in data.iterrows():
        d[index] = {
            'f_want' : row.filter(like='DesireNextYear').sum().sum(),
            'f_know' : row.filter(like='WorkedWith_').sum().sum()
        }
    database_stuff = pd.DataFrame(d)
    
    return database_stuff.T