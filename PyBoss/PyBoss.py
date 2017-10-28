import os
import csv
filenames = ['employee_data1.csv','employee_data2.csv']
for filename in filenames:
    filepath = os.path.join('raw_data',filename)
    out_filepath = os.path.join('rectified_data',filename)
    new_dict = {}
    new_records = []
    state_abbreviator = {'Alaska': 'AK', 'Alabama': 'AL', 'Arkansas': 'AR', 'American Samoa': 'AS', 'Arizona': 'AZ', 'California': 'CA', 'Colorado': 'CO', 'Connecticut': 'CT', 'District of Columbia': 'DC', 'Delaware': 'DE', 'Florida': 'FL', 'Georgia': 'GA', 'Guam': 'GU', 'Hawaii': 'HI', 'Iowa': 'IA', 'Idaho': 'ID', 'Illinois': 'IL', 'Indiana': 'IN', 'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA', 'Massachusetts': 'MA', 'Maryland': 'MD', 'Maine': 'ME', 'Michigan': 'MI', 'Minnesota': 'MN', 'Missouri': 'MO','Northern Mariana Islands': 'MP', 'Mississippi': 'MS', 'Montana': 'MT', 'National': 'NA', 'North Carolina': 'NC', 'North Dakota': 'ND', 'Nebraska': 'NE', 'New Hampshire': 'NH', 'New Jersey': 'NJ', 'New Mexico': 'NM', 'Nevada': 'NV', 'New York': 'NY', 'Ohio': 'OH', 'Oklahoma': 'OK', 'Oregon': 'OR', 'Pennsylvania': 'PA', 'Puerto Rico': 'PR', 'Rhode Island': 'RI', 'South Carolina': 'SC', 'South Dakota': 'SD', 'Tennessee': 'TN', 'Texas': 'TX', 'Utah': 'UT', 'Virginia': 'VA', 'Virgin Islands': 'VI', 'Vermont': 'VT', 'Washington': 'WA', 'Wisconsin': 'WI', 'West Virginia': 'WV', 'Wyoming': 'WY'}


    with open(filepath, 'r') as csvfile:
        csvreader = csv.DictReader(csvfile)

        #Emp ID,Name,DOB,SSN,State
        #Emp ID,First Name,Last Name,DOB,SSN,State
        for row in csvreader:
            new_dict = {}
        
            new_dict['Emp ID'] = row['Emp ID']
        
            name_list = row['Name'].split(' ')
            new_dict['First Name'] = name_list[0]
            new_dict['Last Name'] = name_list[1]
        
            broken_dob = row['DOB'].split('-')
            dob_string = broken_dob[2] + '/' + broken_dob[2] + '/' + broken_dob[0][2:]
            new_dict['DOB'] = dob_string

            broken_SSN = row['SSN'].split('-')
            new_dict['SSN'] = '***-**-' + broken_SSN[2]

            new_dict['State'] = state_abbreviator[row['State']]

            new_records.append(new_dict)

    with open(out_filepath, 'w') as csvfile:
        csvwriter = csv.DictWriter(csvfile, ['Emp ID','First Name','Last Name','DOB','SSN','State'])
        csvwriter.writeheader()
        for row in new_records:
            csvwriter.writerow(row)

        
