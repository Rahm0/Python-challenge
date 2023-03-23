#Import dependancy.

import os
import csv

#Path to collect data from Resources folder. 

csvpath = os.path.join("Resources","budget_data.csv")
output_path = os.path.join("analysis","budget_data_analysis.txt")

#Open csv file as reader.

total_months = 0
months_change = []
net_change_list = []
current_month_profit_loss = 0
net_profit_loss = 0
previous_change_in_profit_lossess = 0
change_in_profit_lossess = 0

#Open and read csv.
with open(csvpath) as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")
    print(csv.reader)

    # Read the header row first.
    csv_header = next(csvfile)
    print(f"Header:{csv_header}")
              
    #Read each row of data after the header.

    for row in csv_reader:

        #Count of months.

        total_months += 1

        #The neT Profit/Losses over the entire period.

        current_month_profit_loss = int(row[1])
        net_profit_loss += current_month_profit_loss

        if (total_months == 1):

            #Make previous month equal to current month.

            previous_change_in_profit_lossess = current_month_profit_loss
            
        else:

            #Calculate profit loss changes.

            change_in_profit_lossess = current_month_profit_loss - previous_change_in_profit_lossess

            #Append each month.

            months_change.append(row[0])

            #Append net change to change in profit_loss.

            net_change_list.append(change_in_profit_lossess)

            #Make loop.

            previous_change_in_profit_lossess = current_month_profit_loss

    #Get sum and average of the changes in Profit/Losses over the entire period.

    sum_profit_loss = sum(net_change_list)
    average = round(sum_profit_loss/(total_months- 1), 2)

    #Highest and lowest changes in Profit/Losses over the entire period.

    highest_change = max(net_change_list)
    lowest_change = min(net_change_list)

    # Highest and lowest revenue.
    
    highest_revenue = net_change_list.index(highest_change)
    lowest_revenue = net_change_list.index(lowest_change)

    # Assign highest and lowest month.
    
    highest_month = months_change[ highest_revenue]
    lowest_month = months_change[lowest_revenue]

# Print.
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {total_months}")
print(f"Total:  ${net_profit_loss}")
print(f"Average Change:  ${average}")
print(f"Greatest Increase in Profits:  {highest_month} (${highest_change})")
print(f"Greatest Decrease in Losses:  {lowest_month} (${lowest_change})")

#Export the result

with open(output_path,"w") as txt_file:
  txt_file.write(f" Financial Analysis\n")
  txt_file.write(f"-------------------------\n")
  txt_file.write(f"Total Months:{total_months}\n")
  txt_file.write(f"Total:${net_profit_loss}\n")
  txt_file.write(f"Average Change:${average}\n")
  txt_file.write(f"Greatest Increase in Profits:  {highest_month} (${highest_change})\n")
  txt_file.write(f"Greatest Decrease in Losses:  {lowest_month} (${lowest_change})")