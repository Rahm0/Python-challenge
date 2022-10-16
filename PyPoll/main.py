import os
import csv
#path to collect data from Resources folder 
csvpath = os.path.join("Resources","election_data.csv")
output_path = os.path.join("analysis","election_analysis.txt")
#open csv file as reader
total_vote_casted = 0
votes = {}

with open(csvpath)as csv_file:
#csv reader specifies delimiter and variable that holds contents 
    csvreader =csv.reader(csv_file, delimiter=',')
    #print(csv.reader)
 #Read the header row first
    csv_header = next(csvreader)
    print(f"Header:{csv_header}")
#Read each row of data after the header
    for row in csvreader:
        print(row)
        total_vote_casted =total_vote_casted +1
        print(total_vote_casted)
        
      


           
with open(output_path,"w")as output_file:
    total_votes_results = (

        f"Election Results\n"
  f"-------------------------\n"
  f"Total Votes: {total_vote_casted}\n"
  f"-------------------------\n"
    )
    print(total_votes_results)

    output_file.write(total_votes_results)
    



