import csv
import os

# total number of votes cast
# complete list of candidates who received votes
# % of votes each candidate won
# total number of votes each candidate won
# winner of election based on popular vote
 
total_number_of_votes = 0
complete_list_of_candidates = []
vote_count = {}
individual_votes = []

csvpath = os.path.join('./Resources/election_data.csv')
# csvoutput = os.path.join('output.txt')
    
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_headers = next(csvreader) # exhausting the first row will leave me with the rest of the data

    for x in csvreader:
        # print(x)
        # ["123455", "Jeffeson", "Charles Casper ...."]
        # ["987654", "Jeffeson", "Charles Casper ...."]
        total_number_of_votes += 1
    
        name = x[2] 

        if name not in complete_list_of_candidates:

            complete_list_of_candidates.append(name)
            vote_count[name] = 1
        else: # if the candidate already exist, just increment the value for the name by 1
            vote_count[name] += 1

    print(f"Election Results")
    print(f"Total Votes: " + str(total_number_of_votes))
    for k, v in vote_count.items():
        print(f" {k} {round(v/total_number_of_votes*100,2)}% ( {v}  )")
        
   # for k, v in vote_count.items():
    #    print(f"{k} : ( {v} )")

    max_votes = 0
    name = ""

    for k,v in vote_count.items():
        if max_votes < v: # 0 < 85213 , 85213 < 272892
            max_votes = v
            name = k
        else:
            continue
    print(f"Winner: {name} ( {max_votes})")



         



    
    






