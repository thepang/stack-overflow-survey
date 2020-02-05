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
    'BetterLife' : {
        'Yes' : 1,
        'No' : 0
    },
    'Dependents' : {
        'Yes' : 1,
        'No' : 0
    },
    'FizzBuzz' : {
        'Yes' : 1,
        'No' : 0        
    },
    'Trans' : {
        'Yes' : 1,
        'No' : 0  
    },

    
    'Student' : {
        'No' : 0,
        'Yes, full-time' : .5,
        'Yes, part-time' : 1
    },
    'MgrMoney' : {
        'Not sure' : 0.5,
        'Yes' : 1,
        'No' : 0
    },
    'MgrWant' : {
        'Not sure' : .5,
        'No' : 0,
        'Yes' : 1,
        'I am already a manager' : 0
    },
    'MgrIdiot' : {
        'Very confident' : 3,
        'Somewhat confident' : 2,
        'Not at all confident' : 1,
        "I don't have a manager" : 0 
    },
    'OpenSourcer' : {
        'Never' : 0,
        'Less than once per year' : 1,
        'Less than once a month but more than once per year' : 4,
        'Once a month or more often' : 13,
    },
    'PurchaseWhat' : {
        'I have little or no influence' : 0,
        'I have some influence' : .5,
        'I have a great deal of influence' : 1
    },
    'OpenSource' : {
        'The quality of OSS and closed source software is about the same' : .5,
        'OSS is, on average, of HIGHER quality than proprietary / closed source software' : 1,
        'OSS is, on average, of LOWER quality than proprietary / closed source software' : 0
    },
    'SurveyEase' : {
        'Easy' : 0,
        'Neither easy nor difficult' : 0.5,
        'Difficult' : 1
    },
    'SurveyLength' : {
        'Appropriate in length' : 0.5,
        'Too long' : 1,
        'Too short' : 0
    },
    'ImpSyn' : {
        'Far below average' : 0,
        'A little below average' : .25,
        'Average' :  .5,
        'A little above average' : .75,
        'Far above average' : 1
    },

    
    
    
    'LastHireDate' : {
        'Less than a year ago' : 0,
        '1-2 years ago' : 1,
        'More than 4 years ago' : 5,
        '3-4 years ago': 3,
        'NA - I am an independent contractor or self employed' : 0,
        "I've never had a job" : 0
    },
    'SOPartFreq' : {
        'Less than once per month or monthly' : 1,
        'I have never participated in Q&A on Stack Overflow' : 0,
        'A few times per month or weekly' : 5,
        'A few times per week' : 10,
        'Daily or almost daily' : 20,
        'Multiple times per day' : 40
     },
    'OrgSize' : {
        '20 to 99 employees' : 20,
        '100 to 499 employees' : 100,
        '10,000 or more employees' : 10000,
        '1,000 to 4,999 employees' : 1000,
        '10 to 19 employees': 10,
        '2-9 employees' : 2,
        '500 to 999 employees' : 500,
        '5,000 to 9,999 employees' : 5000,
        'Just me - I am a freelancer, sole proprietor, etc.' : 0
    },
    'SOVisitFreq' : {
        'Multiple times per day': 1000,
        'Daily or almost daily' : 365,
        'A few times per week' : 100,
        'A few times per month or weekly' : 30, 
        'Less than once per month or monthly' : 12,
        'I have never visited Stack Overflow (before today)' : 0
    },
    'WorkRemote' : {
        'Less than once per month / Never' : 0,
        'A few days each month' : 3,
        'Less than half the time, but at least one day each week' : 5,
        "All or almost all the time (I'm full-time remote)" : 20,
        "It's complicated" : 0,
        'More than half, but not all, the time' : 15,
        'About half the time' : 10
    },

    
    
    'Age1stCode' : {
        'Younger than 5 years' : 3,
        'Older than 85' : 90
    },
    'YearsCode' : {
        'Less than 1 year' : 0,
        'More than 50 years' : 52
    },
    'YearsCodePro' : {
        'Less than 1 year' : 0,
        'More than 50 years' : 52
    }

}

country_to_region = {
    'United States' : 'United States',
    
    'Israel' : 'MiddleEast',
    'Iran' : 'MiddleEast',
    'Jordan' : 'MiddleEast',
    'Iraq' : 'MiddleEast',
    'Syrian Arab Republic' : 'MiddleEast',
    'Yemen' : 'MiddleEast',
    'Qatar' : 'MiddleEast',
    'Oman' : 'MiddleEast',
    'United Arab Emirates' : 'MiddleEast',
    'Saudi Arabia' : 'MiddleEast',
    'Lebanon' : 'MiddleEast',
    'Bahrain' : 'MiddleEast',
    'Kuwait' : 'MiddleEast',
    
    'Australia' : 'Oceania',
    'New Zealand' : 'Oceania',
    'Fiji' : 'Oceania',
    'Papua New Guinea' : 'Oceania',
    'Tonga' : 'Oceania',
    
    'Brazil' : 'Americas',
    'Canada' : 'Americas',
    'Mexico' : 'Americas',
    'Argentina' : 'Americas',
    'Colombia' : 'Americas',
    'Antigua and Barbuda' : 'Americas',
    'Haiti' : 'Americas',
    'Barbados' : 'Americas',
    'Bahamas' : 'Americas',
    'Saint Vincent and the Grenadines' : 'Americas',
    'Dominica' : 'Americas',
    'Saint Kitts and Nevis' : 'Americas',
    'Guyana' : 'Americas',
    'Belize' : 'Americas',
    'Guatemala' : 'Americas',
    'El Salvador' : 'Americas',
    'Paraguay' : 'Americas',
    'Costa Rica' : 'Americas',
    'Ecuador' : 'Americas',
    'Chile' : 'Americas',
    'Peru' : 'Americas',
    'Nicaragua' : 'Americas',
    'Honduras' : 'Americas',
    'Venezuela, Bolivarian Republic of...' : 'Americas',
    'Uruguay' : 'Americas',
    'Panama' : 'Americas',
    'Bolivia' : 'Americas',
    'Cuba' : 'Americas',
    'Jamaica' : 'Americas',
    'Trinidad and Tobago' : 'Americas',
    'Dominican Republic' : 'Americas',
    
    'United Kingdom' : 'Europe',
    'Germany' : 'Europe',
    'France' : 'Europe',
    'Norway' : 'Europe',
    'Finland' : 'Europe',
    'Ireland' : 'Europe',
    'Denmark' : 'Europe',
    'Portugal' : 'Europe',
    'Greece' : 'Europe',
    'Hungary' : 'Europe',
    'Slovenia' : 'Europe',
    'Serbia' : 'Europe',
    'Lithuania' : 'Europe',
    'Croatia' : 'Europe',
    'Spain' : 'Europe',
    'Poland' : 'Europe',
    'Italy' : 'Europe',
    'Czech Republic' : 'Europe',
    'Romania' : 'Europe',
    'Austria' : 'Europe',
    'Bulgaria' : 'Europe',
    'Belgium' : 'Europe',
    'Switzerland' : 'Europe',
    'Turkey' : 'Europe',
    'Ukraine' : 'Europe',
    'Sweden' : 'Europe',
    'Netherlands' : 'Europe',
    'Russian Federation' : 'Europe',
    'Netherlands' : 'Europe',
    'Andorra' : 'Europe',
    'Liechtenstein' : 'Europe',
    'San Marino' : 'Europe',
    'Malta' : 'Europe',
    'Cyprus' : 'Europe',
    'Luxembourg' : 'Europe',
    'The former Yugoslav Republic of Macedonia' : 'Europe',
    'Iceland' : 'Europe',
    'Latvia' : 'Europe',
    'Bosnia and Herzegovina' : 'Europe',
    'Albania' : 'Europe',
    'Slovakia' : 'Europe',
    'Estonia' : 'Europe',
    'Monaco' : 'Europe',
    'Montenegro' : 'Europe',
    'Republic of Moldova' : 'Europe',
    'Belarus' : 'Europe',

    "Democratic People's Republic of Korea" : 'Asia',
    'Pakistan' : 'Asia',
    'China' : 'Asia',
    'Bangladesh' : 'Asia',
    'Japan' : 'Asia',
    'Indonesia' : 'Asia',
    'Sri Lanka' : 'Asia',
    'Singapore' : 'Asia',
    'Philippines' : 'Asia',
    'Malaysia' : 'Asia',
    'North Korea' : 'Asia',
    'Tajikistan' : 'Asia',
    'Turkmenistan' : 'Asia',
    "Lao People's Democratic Republic" : 'Asia',
    'Bhutan' : 'Asia',
    'Brunei Darussalam' : 'Asia',
    'Timor-Leste' : 'Asia',
    'Hong Kong (S.A.R.)' : 'Asia',
    'Taiwan' : 'Asia',
    'South Korea' : 'Asia',
    'Republic of Korea' : 'Asia',
    'Myanmar' : 'Asia',
    'Mongolia' : 'Asia',
    'Viet Nam' : 'Asia',
    'Thailand' : 'Asia',
    'Cambodia' : 'Asia',
    'Armenia' : 'Asia',
    'Georgia' : 'Asia',
    'Kazakhstan' : 'Asia',
    'Azerbaijan' : 'Asia',
    'Afghanistan' : 'Asia',
    'Uzbekistan' : 'Asia',
    'Kyrgyzstan' : 'Asia',
    'Maldives' : 'Asia',
    'Nepal' : 'Asia',
    
    'Nigeria' : 'Africa',
    'South Africa' : 'Africa',
    'Democratic Republic of the Congo' : 'Africa',
    'Libyan Arab Jamahiriya' : 'Africa',
    'Swaziland' : 'Africa',
    'Mozambique' : 'Africa',
    'Mauritania' : 'Africa',
    'Congo, Republic of the...' : 'Africa',
    'Namibia' : 'Africa',
    'Botswana' : 'Africa',
    'Angola' : 'Africa',
    'Liberia' : 'Africa',
    'Chad' : 'Africa',
    'Djibouti' : 'Africa',
    'Niger' : 'Africa',
    'Benin' : 'Africa',
    'Togo' : 'Africa',
    'Sao Tome and Principe' : 'Africa',
    'Burkina Faso' : 'Africa', 
    'Mali' : 'Africa',
    'Guinea' : 'Africa',
    'Cape Verde' : 'Africa',
    'Burundi' : 'Africa',
    'Sierra Leone' : 'Africa',
    'Gabon' : 'Africa',
    'Malawi' : 'Africa',
    'Lesotho' : 'Africa',
    'Uganda' : 'Africa',
    'Ethiopia' : 'Africa',
    'Cameroon' : 'Africa',
    'Madagascar' : 'Africa',
    'Sudan' : 'Africa',
    'Somalia' : 'Africa',
    'Rwanda' : 'Africa',
    'Zambia' : 'Africa',
    'Zimbabwe' : 'Africa',
    'Egypt' : 'Africa',
    'Ghana' : 'Africa',
    'Kenya' : 'Africa',
    'Algeria' : 'Africa',
    'Tunisia' : 'Africa',
    "Côte d'Ivoire" : 'Africa',
    'United Republic of Tanzania' : 'Africa',
    'Mauritius' : 'Africa',
    'Senegal' : 'Africa',
    'Morocco' : 'Africa',
    'Seychelles' : 'Africa',
    
    'Other Country (Not Listed Above)' : 'OtherCountry'

}