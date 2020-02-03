import pandas as pd

survey_values ={
    'JobSat' : {
        'Very satisfied' : 1,
        'Slightly satisfied' : 1,
        'Slightly dissatisfied' : 0,
        'Very dissatisfied' : 0,
        'Neither satisfied nor dissatisfied' : 0
    },    
    'Hobbyist' : {
        'Yes' : 1,
        'No' : 0
    },
    'OpenSourcer' : {
        'Never' : 0,
        'Less than once per year' : 1,
        'Less than once a month but more than once per year' : 4,
        'Once a month or more often' : 13,
    },
    'LastHireDate' : {
        'Less than a year ago' : 0,
        '1-2 years ago' : 1,
        'More than 4 years ago' : 5,
        '3-4 years ago': 3,
        'NA - I am an independent contractor or self employed' : 0,
        "I've never had a job" : 0
    },
    'SOVisitFreq' : {
        'Multiple times per day': 1000,
        'Daily or almost daily' : 365,
        'A few times per week' : 100,
        'A few times per month or weekly' : 30, 
        'Less than once per month or monthly' : 12,
        'I have never visited Stack Overflow (before today)' : 0
    },
    'YearsCode' : {
        'Less than 1 year' : 0,
        'More than 50 years' : 52
    },
    'MgrIdiot' : {
        'Very confident' : 3,
        'Somewhat confident' : 2,
        'Not at all confident' : 1,
        "I don't have a manager" : 0 
    }
}

def response_map():
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
    Returns dataframe with columns that only contain columns that are not part of survey_results.
    Columns that I've determined are not needed are also not returned.
    """
    culled = remove_unneeded_data(data)
    for column in survey_values.keys():
        if column!='JobSat':
            culled = culled.drop(columns=[column])
        
    culled = culled.drop(columns=['CurrencySymbol', 'CurrencyDesc', 'CompTotal', 'CompFreq', 'MainBranch', 'Employment'])
    
    return culled


def replace_data(data, mapping_dictionary):
    """
    Returns a new dataframe with columns that correspond to the keys in mapping_dctionary.
    All the values in the columns are updated using the values in mapping_dictionary.
    """
    new_df = pd.DataFrame()
    
    for column in mapping_dictionary.keys():
        new_df[column] = data[column]

    new_df = new_df.replace(mapping_dictionary) 
    return new_df


def fill_nans(data):
    """
    Returns dataframe with NaNs filled with mean.
    """
    # Filter column for non null values, get the mean for those values and then fill the NaNs with that value.
    if 'YearsCode' in data.columns:
        data['YearsCode'] = data['YearsCode'].fillna(data['YearsCode'].dropna().astype('int64').mean())
        data['YearsCode'] = data['YearsCode'].astype('int64')
    data = data.fillna(data.mean())
    return data
    

def get_analysis_data(raw_data):
    """
    Returns the new dataframe. New datafram's columns correspond to keys in survey_values.
    NaNs are filled with means.
    """
    
    culled = remove_unneeded_data(raw_data)
    mapped = replace_data(culled, survey_values)

    return fill_nans(mapped)

"""
replace_map = {
    "LastHireDate": {
        "Less...", 0,
        
    }
}
surprises = set()
"""