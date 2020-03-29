import os
import csv

# I had a nightmare working with my file path, the current working directory is the only solution I could deploy
current_environment = str(os.getcwd())
poll_csv = str(os.path.join(current_environment,'Class','Homework','python-challenge','Resources','election_data.csv'))

# Initialize empty dictionary and vote count variable
candidates = {}
i = 0
vote_tally = 1

#Opens bank file
with open(poll_csv) as poll_file:

    # Creates reader and skips header row
    my_reader = csv.reader(poll_file)
    next(my_reader)

    # Loops through rows, adding unique candidate values to candidates dictionary and incrementing vote count
    for row in my_reader:
        candidate = str(row[2])
        if not candidate in candidates.keys():
            candidates[candidate] = 1
        else:
            candidates[candidate] = candidates[candidate] + 1
        vote_tally = vote_tally + 1
   
#Loops through dictionary creating candidate name/vote count string    
vote_by_candidate= ""
for key in candidates:
    vote_by_candidate = str(vote_by_candidate) + "\n" + str(key) + " " + str(round(candidates[key]/vote_tally*100)) + "% " + str(candidates[key])

# Creates list of candidates and values to find max vote total and apply that index to candidate list
cand_list = list(candidates.keys())
vote_list = list(candidates.values())
max_index = vote_list.index(max(vote_list))
winner = cand_list[max_index]

# Creates final report string for console print and text file creation
final_print = "Election Results" + "\n"
final_print = final_print + "---------------------------" + "\n"
final_print = final_print + "Total Votes: " + str(vote_tally) + "\n" + "---------------------------" + "\n"
final_print = final_print + str(vote_by_candidate) + "\n" + "---------------------------" + "\n"
final_print = final_print + "Winner: " + str(winner) + "\n" + "---------------------------"
print(final_print)

# writes text to file
write_string = os.path.join(current_environment, "Class", "Homework","python-challenge", "py_poll_text.txt")
with open(write_string,"w") as createfile:
    createfile.write(final_print)
    createfile.close()