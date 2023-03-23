#Import dependancy.

import os
import csv

#Path to collect data from Resources folder. 

csvpath = os.path.join("Resources","election_data.csv")
output_path = os.path.join("analysis","election_analysis.txt")

#Open csv file as reader.

total_vote_casted= 0
candidate = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open CSV.

with open(csvpath)as csv_file:

#Csv reader specifies delimiter and variable that holds contents.

    csvreader =csv.reader(csv_file, delimiter=',')
    #print(csv.reader)

 #Read the header row first.

    csv_header = next(csvreader)
    print(f"Header:{csv_header}")

#Read each row of data after the header.

    for row in csvreader:
       # print(row)
        #Add to the total vote count.
        total_vote_casted =total_vote_casted +1
        #Find the candidate name from each row.
        candidate_name = row[2]
        
        if candidate_name not in candidate:
           
            candidate.append(candidate_name)
            
            candidate_votes[candidate_name] = 0
        
        candidate_votes[candidate_name] += 1

#Save the results to text file.

with open(output_path, "w") as txt_file:

    #Print the final vote.

    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_vote_casted :,}\n"
        f"-------------------------\n")
    print(election_results, end="")

    #Export the result.

    txt_file.write(election_results)
    for candidate in candidate_votes:

        #Retrieve vote count and percentage.

        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_vote_casted ) * 100
        candidate_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

        #Print results.

        print(candidate_results)
        # Save the result.

        txt_file.write(candidate_results)

        #Determine winning votes.

        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate
           
    #Print the winning candidate's results.

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    #Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)