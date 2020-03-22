# import modules
import os
import csv

# Set path for file
csvpath = os.path.join("Resources/election_data.csv")

# Create empty variables
TotalVotes = 0
CandidatesList = []
VotesByCandidate = {}
VoteCountForLeader = 0

# Open the CSV
with open(csvpath, newline="") as csvfile:
    
    # store CSV file as a dictionary in a variable
    csvreader = csv.DictReader(csvfile, delimiter=",")
    
    # iterate through rows in CSV file
    for row in csvreader:
        candidate = row['Candidate']
        CandidatesList.append(candidate)
        VotesByCandidate[candidate] = 0    
        VotesByCandidate[candidate]=VotesByCandidate[candidate] + 1
        TotalVotes = TotalVotes + 1
        
        if VotesByCandidate[candidate] > VoteCountForLeader :
            VoteCountForLeader = VotesByCandidate[candidate]
            VoteLeader = candidate

 # print total votes
    print("Election Results")
    print("-------------------------")
    print("Total Votes " + str(TotalVotes))
    print("-------------------------")

 # print each candidate and corresponding votes
    for i in VotesByCandidate:
        print(i + " " + str(round(((VotesByCandidate[i]/TotalVotes)*100))) + "%" + " (" + str(VotesByCandidate[i]) + ")") 
   
 # print winner
    print("-------------------------")
    print("Winner: " + VoteLeader)
    print("-------------------------")

# set path for output file
output_file = os.path.join("output.csv")

# open the output file, 
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)

    writer.write("Election Results")
    writer.write("-------------------------")
    writer.write("Total Votes " + str(TotalVotes))
    writer.write("-------------------------")

    for i in VotesByCandidate:
        writer.write(i + " " + str(round(((VotesByCandidate[i]/TotalVotes)*100))) + "%" + " (" + str(VotesByCandidate[i]) + ")") 
   
    writer.write("-------------------------")
    writer.write("Winner: " + VoteLeader)
    writer.write("-------------------------")