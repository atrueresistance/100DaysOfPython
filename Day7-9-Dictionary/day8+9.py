us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}


states_list = ['Oklahoma',
               'Kansas',
               'North Carolina',
               'Georgia',
               'Oregon',
               'Mississippi',
               'Minnesota',
               'Colorado',
               'Alabama',
               'Massachusetts',
               'Arizona',
               'Connecticut',
               'Montana',
               'West Virginia',
               'Nebraska',
               'New York',
               'Nevada',
               'Idaho',
               'New Jersey',
               'Missouri',
               'South Carolina',
               'Pennsylvania',
               'Rhode Island',
               'New Mexico',
               'Alaska',
               'New Hampshire',
               'Tennessee',
               'Washington',
               'Indiana',
               'Hawaii',
               'Kentucky',
               'Virginia',
               'Ohio',
               'Wisconsin',
               'Maryland',
               'Florida',
               'Utah',
               'Maine',
               'California',
               'Vermont',
               'Arkansas',
               'Wyoming',
               'Louisiana',
               'North Dakota',
               'South Dakota',
               'Texas',
               'Illinois',
               'Iowa',
               'Michigan',
               'Delaware']


def index(list, item_number):
    cnt = 1
    for item in list:
        if cnt == item_number:
            return item
        cnt += 1


# Print out the 10th item in each.
print("Print out the 10th item in each list.")
print(index(us_state_abbrev, 10), us_state_abbrev[index(us_state_abbrev, 10)])
print(index(states_list, 10))

# Print out the 45th key in the dictionary.
print("\n\nPrint out the 45th key in the dictionary")
print(index(us_state_abbrev, 45))
print(index(states_list, 45))

# Print out the 27th value in the dictionary.
print("\n\nPrint out the 27th value in the dictionary.")
print(us_state_abbrev[index(us_state_abbrev, 45)])