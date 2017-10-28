import os
import csv
import sys 
import pandas as pd

filename = 'election_data_2.csv'
out_filename = 'election_results.txt'
out_filename_csv = 'election_result_data'
filepath = os.path.join('raw_data', filename)
out_filepath = os.path.join('processed_data', out_filename)
out_filepath_csv = os.path.join('processed_data', out_filename_csv)
candidates = []#'Khan', 'Correy', 'Li', "O'Tooley"]
votes = {}#'Khan': 0, 'Correy': 0, 'Li': 0, "O'Tooley": 0}
county_vote = {}#'Marsh': {'Khan': 0, 'Correy': 0, 'Li': 0, "O'Tooley": 0}, 'Queen':{'Khan': 0, 'Correy': 0, 'Li': 0, "O'Tooley": 0}, 'Bamoo': {'Khan': 0, 'Correy': 0, 'Li': 0, "O'Tooley": 0}, 'Trandee': {'Khan': 0, 'Correy': 0, 'Li': 0, "O'Tooley": 0}, 'Raffah': {'Khan': 0, 'Correy': 0, 'Li': 0, "O'Tooley": 0}}
counties = []
voter_ids = []
vote_total = 0
winner = {}

with open(filepath, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    
    next(csvreader)

    print("\nCOUNTING VOTES")
    print('____________________________________________________________________')

    for row in csvreader:
        # create key in votes
        if row[2] not in votes:
            votes[row[2]] = 0
            candidates.append(row[2])
        # tally vote in votes
        votes[row[2]] += 1

        # create keys in county_vote
        if row[1] not in county_vote:
            county_vote[row[1]] = {}
            counties.append(row[1])
        if row[2] not in county_vote[row[1]]:
            county_vote[row[1]][row[2]] = 0
        # tally vote in county_vote
        county_vote[row[1]][row[2]] += 1

        vote_total += 1
        if vote_total % 51500 == 0:            
            print("#", end = '')
            sys.stdout.flush()

        #if row[0] in voter_ids:
        #    print(f"ERROR - VOTER FRAUD DETECTED {row}")
        #voter_ids.append(row[0])
print('\n')

with open(out_filepath, 'w') as textfile:

    print("====================================================================")
    textfile.write("Election Results====================================================\n")

    #COUNTY PRINTOUT
    for county in county_vote:
        print(f'{county} County --------------')
        textfile.write(f'{county} County --------------\n')
        #pulls candidates from list to order printout
        county_vote_total = 0
        #gets county vote totals

        for candidate in county_vote[county]:
            county_vote_total += county_vote[county][candidate]
        #prints out vounty votes by pulling candidates from list to order printout
        for candidate in candidates:
            #avoids possible keyerrors from candidates not running in a given county
            if candidate in county_vote[county]:
                print(f"{candidate}: {county_vote[county][candidate]}", end = "\t")
                textfile.write(f"{candidate}: {county_vote[county][candidate]} \t")
        #prints out county percentages
        print('')
        textfile.write('\n')
        for candidate in candidates:
            #avoids possible keyerrors from candidates not running in a county
            if candidate in county_vote[county]:
                print(f'{candidate}: {int(round(county_vote[county][candidate]/county_vote_total*100,0))}%   ', end = '\t')
                textfile.write(f'{candidate}: {int(round(county_vote[county][candidate]/county_vote_total*100,0))}%   \t')
        print('')
        textfile.write('\n')

    #VOTE TOTAL PRINTOUT
    print("====================================================================")
    textfile.write("====================================================================\n")
    print(f'Total Votes: {vote_total}')
    textfile.write(f'Total Votes: {vote_total}\n')
    for candidate in votes:
        print(f'{candidate}: {votes[candidate]}', end = '\t')
        textfile.write(f'{candidate}: {votes[candidate]} \t')
    print('')
    textfile.write('\n')

    #PERCENTAGE PRINTOUT
    last_total = 0
    for candidate in votes:
        print(f'{candidate}: {int(round(votes[candidate]/vote_total*100,0))}%    ', end = '\t')
        textfile.write(f'{candidate}: {int(round(votes[candidate]/vote_total*100,0))}%    \t')
        if votes[candidate] > last_total:
            winner = [candidate, int(round(votes[candidate]/vote_total*100,0))]
            last_total = votes[candidate]

    print('')
    textfile.write('\n')
    print(f'WINNER - {winner[0]} with {winner[1]}% of the vote.')
    textfile.write(f'WINNER - {winner[0]} with {winner[1]}% of the vote.\n')

counties.append(votes)
df = pd.DataFrame(counties)
print(df)
df.to_csv(out_filepath_csv, ',')

