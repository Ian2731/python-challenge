import os
import csv

py_poll = os.path.join("PyPoll", "election_data.csv")

total = 0

with open(py_poll, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)

    voters = []

    county = []

    candidate = []

    unique_candidate = []

    castvotes = []

    candidatedetail = []

    for row in csvreader:
        voters.append(row[0])
        county.append(row[1])
        candidate.append(row[2])


print("Election Results")
print("------------------")
print(f"Total Votes: {len(voters)}")
print("------------------")

for x in candidate:
    if x not in unique_candidate:
        unique_candidate.append(x)
        castvotes.append(candidate.count(x))
        print(f"{(x)}: {round((candidate.count(x)/len(voters))* 100, 3)} % ({candidate.count(x)})")
        candidatedetail.append(f"{(x)}: {round((candidate.count(x)/len(voters))* 100, 3)} % ({candidate.count(x)})")

max_winner = str(unique_candidate[castvotes.index(max(castvotes))])
print("-----------------")
print(f"Winner: {max_winner}")

fh = open("pypoll.txt", "w")
fh.write("Election Results\n"
    "----------------------------\n"
    f"Total Votes: {len(voters)}\n"
    "----------------------------\n")

for i in range(len(candidatedetail)):
    fh.write(
        f"{candidatedetail[i]}\n"
    )
fh.write("-----------------\n"
        f"Winner: {max_winner}")
fh.close()