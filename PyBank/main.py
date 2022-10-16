import os
import csv
#path to collect data from Resources folder 
csvpath = os.path.join("Resources","budget_data.csv")
output_path = os.path.join("analysis","budget_data_analysis.txt")
#open csv file as reader
total_months = 0
net_change_list = []
total_netprofit_lossess=0
change_in_profit_lossess =0
previous_change_in_profit_lossess =0
months_change = []

with open(csvpath)as csv_file:
#csv reader specifies delimiter and variable that holds contents 
    csvreader =csv.reader(csv_file, delimiter=',')
    print(csv.reader)
 #Read the header row first
    csv_header = next(csvreader)
    print(f"Header:{csv_header}")
#Read each row of data after the header
    for row in csvreader:
        print(row)
        total_months =total_months +1
           
        print(total_months)

#the net total amount of "Profit/Losses" over the entire perio
        total_netprofit_lossess= total_netprofit_lossess + int(row[1])

        print(total_netprofit_lossess)
       
# The changes in "Profit/Losses" over the entire period, and then the average of those changes
        change_in_profit_lossess = int(previous_change_in_profit_lossess)-int(row[1]) 
        previous_change_in_profit_lossess =(row[1])
        months_change.append (change_in_profit_lossess)
        
        # print(months_change)

#The average change
        average = sum(months_change) / len (months_change)
        print(average)

#Export the result
with open(output_path,"w") as txt_file:
  txt_file.write(f" Financial Analysis\n")
  txt_file.write(f"-------------------------\n")
  txt_file.write(f"Total Months:{total_months}\n")
  txt_file.write(f"Total:${total_netprofit_lossess}\n")
  txt_file.write(f"Average Change:${average}\n")



