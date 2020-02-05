import pandas as pd
import dictionaries as d

def get_dictionary():
    return d.sdf

def response_map(value=''):
    return survey_values

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
    
    
def unused_data(data):
    """
    Returns dataframe with columns that only contain columns
    that are not part of survey_values (except JobSat).
    Columns that I've determined are not needed are also not returned.
    """
    culled = remove_unneeded_data(data)
    for column in survey_values.keys():
        if column!='JobSat':
            culled = culled.drop(columns=[column])
        
    culled = culled.drop(columns=['CurrencySymbol', 'CurrencyDesc', 'CompTotal', 'CompFreq', 'MainBranch', 'Employment'])
    
    return culled


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
        elif column in ['BetterLife', 'Dependents', 'Hobbyist', 'Student', 'MgrMoney', 'MgrWant', 'MgrIdiot', 'OpenSourcer' , 'PurchaseWhat', 'OpenSource', 'FizzBuzz', 'Trans', 'SurveyEase', 'SurveyLength']:
            new_mode = data[column].mode()
            data[column] = data[column].fillna(new_mode[0])
        else:
            data[column] = data[column].fillna(data[column].mean())
    return data


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
        
    ###### 4. Fill the nans (custom logic in fill_nans function)
    to_return = fill_nans(mapped)

    return to_return