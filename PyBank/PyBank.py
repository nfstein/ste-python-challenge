import os
import csv
entries = []
changes = []
filenames = ['budget_data_1.csv', 'budget_data_2.csv']
last_entry = 1

for filename in filenames:
    filepath = os.path.join('raw_data', filename)

    with open(filepath, 'r') as csvfile:
        csvreader = csv.reader(csvfile,)
        next(csvreader, None)
        for row in csvreader:
            entry = [row[0],int(row[1])]
            entries.append(entry)
            changes.append((int(row[1])-last_entry))
            last_entry = int(row[1])


total_months = len(entries)
total_revenue = 0
last_entry = [entries[0][0], (entries[0][1])]
greatest_revenue = [entries[0][0], (entries[0][1]-1)]
least_revenue = [entries[0][0], (entries[0][1]+1)]

average_change = 0

#first entry of changes is dud data b/c first month has no prior month to compare to
for i in range(1,len(changes)):
    average_change += changes[i]
average_change = average_change/(len(changes)-1)

for entry in entries:
    total_revenue += entry[1]
    if entry[1] > greatest_revenue[1]:
        greatest_revenue = entry
    if entry[1] < least_revenue[1]:
        least_revenue = entry    
    last_entry = entry

average_revenue = total_revenue / total_months

print('REVENUE REPORT ==========================')
print(f'Total Months: {total_months}')
print(f'Total Revenue: {total_revenue}')
print(f'Average Revenue: {average_revenue}')
print(f'Average Change in Revenue: {average_change}')
print(f'Greatest Revenue: {greatest_revenue[0]}, {greatest_revenue[1]}')
print(f'Least Revenue: {least_revenue[0]}, {least_revenue[1]}')
print(f'Average Revenue: {average_revenue}')



