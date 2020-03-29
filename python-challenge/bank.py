import os
import csv

# I had a nightmare working with my file path, the current working directory is the only solution I could deploy
current_environment = str(os.getcwd())
bank_csv = str(os.path.join(current_environment,'Class','Homework','python-challenge','Resources','03_hw_bank.csv'))

# Opens bank file
with open(bank_csv) as bank_file:

# Sets reader object and advances past header row
    my_reader = csv.reader(bank_file)
    next(my_reader)

    # Set initial variables to 0 and initialize empty lists
    profit = 0
    diff_list = []
    month_list = []
    old_val = 0

    # Goes through row values......
    for row in my_reader:

        # subracting previous row value from current row value......
        new_val = int(row[1])
        diff = new_val - old_val

        # appending month change and month name to appropriate list.......
        diff_list.append(diff)
        month_list.append(row[0])

        # and incrementing profit/loss value......
        profit = profit + int(row[1])

        # and setting current row profit/loss value as previous row value before looping to next row
        old_val = int(row[1])

    # Sets max/min profit and index values for same
    max_profit = "{:,}".format(max(diff_list))
    min_profit = "{:,}".format(min(diff_list))
    max_index = diff_list.index(max(diff_list))
    min_index = diff_list.index(min(diff_list))

    #  Uses index values to return max/min month
    max_month = month_list[max_index]
    min_month = month_list[min_index]
    
    #  Sets average profit/loss
    month_count = len(month_list)
    profit_average = "{:,}".format(round(profit/month_count))
    profit = "{:,}".format(profit)

####### Output section, concats print lines into single variable for console print and file write #######
print_text = "Financial Analysis\n"
print_text = print_text + "-----------------------------\n"
print_text = print_text + "Number of Months: " + str(month_count) + "\n"
print_text = print_text + "Total: " + str(profit) + "\n"
print_text = print_text + "Average Change: " + str(profit_average) + "\n"
print_text = print_text + "Greatest Increase in Profits: " +str(max_month) + " " + str(max_profit) + "\n"
print_text = print_text + "Greatest Decrease in Profits: " +str(min_month) + " " + str(min_profit) + "\n"
print(print_text)

# writes text to file
write_string = os.path.join(current_environment, "Class", "Homework","python-challenge", "bank_text.txt")
print(str(write_string))
print(current_environment)
with open(write_string,"w") as createfile:
    createfile.write(print_text)
    createfile.close()