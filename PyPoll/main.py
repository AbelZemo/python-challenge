import csv #import csv
import os #import operating system


# Get the current working directory (cwd)
cwd = os.getcwd() 

# get the file path
file1 = cwd + os.path.join("\\python-challenge","PyPoll","Resources", "election_data.csv")

#open election data and read the first row which is header row
with open(file1, newline="") as csv_file:
    csvreader=csv.reader(csv_file, delimiter=",")
    csvheader=next(csvreader)
    #list comprehension. basically addd candidates into a list of the row of candidate in the file, [2] starts at row 2
    candidate_roster=[candidate[2] for candidate in csvreader]

#calculate the number of votes. We can use len to count the votes by counting the rows of candidate_roster
vote_total=len(candidate_roster)

#List comprehension. Give me the candidate and the amount of votes they have from the dataset that we created earlier (candidate roster)
#how many ballots have the candidates names on it
candidate_votes=[[candidate,candidate_roster.count(candidate)] for candidate in set(candidate_roster)]

candidates_sorted=sorted(candidate_votes, key=lambda x:x[1], reverse=True)

# #2 and #4 solved on module 3 challenges. Able to list Candidates that recieved votes as well as how much each got 

#get all the candidates in the index and divide them by vote total. Then multiply by 100 to get percentage
for candidate in candidates_sorted:
    percentage=(candidate[1]/vote_total)*100
    print(f'{candidate[0]}:{percentage:6.3f}%({candidate[1]})') #! 
#3

#print the final winner
#We use the function on candidates sorted because it has the candidates ordered from Descending order. With that, the index [0][0] will always have the winner of the poll.
#ripnt(f'{candidates_sorted[0][0]}') !

print("--------------------------------------------")
print("The total of votes are "+ str(vote_total))
print(candidates_sorted)
print("Above are the candidates who recieved votes")
for candidate in candidates_sorted:
    percentage=(candidate[1]/vote_total)*100
    print(f'{candidate[0]}: {percentage:6.3f}% ({candidate[1]}) Candidate info')
print(f'{candidates_sorted[0][0]} is the winner')


# get the file path
file2 = cwd + os.path.join("\\python-challenge","PyPoll","Analysis", "pyPollAnalysis.txt")

with open(file2, "w") as txt_file:
    print("--------------------------------------------", file=txt_file)
    print("The total of votes are "+ str(vote_total), file=txt_file)
    print(candidates_sorted, file=txt_file)
    print("Above are the candidates who recieved votes", file=txt_file)
    for candidate in candidates_sorted:
        percentage=(candidate[1]/vote_total)*100
        print(f'{candidate[0]}: {percentage:6.3f}% ({candidate[1]}) Candidate info', file=txt_file)
    print(f'{candidates_sorted[0][0]} is the winner', file=txt_file)