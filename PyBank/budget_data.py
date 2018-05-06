# import needed modules
import os

# Module for reading CSV's
import csv

csvpath = "budget_data_1.csv"
output_path = "new_budget_data.csv"

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # Skip the Headers
    next(csvreader,None)
    #  Initilize String Variables
    previous_month = " "
    first_record = "y"
    #  Initialize totals
    total_months = 0
    total_revenue = 0
    total_change_in_revenue = 0
    previous_revenue = 0
    month_revenue = 0
    max_revenue = 0
    min_revenue = 0
    avg_change = 0
    # Empty List for Revenue Values
    revenue_lst =[]
    # Empty List for Dates
    date_lst = []
    # Empty List for Financial Analysis Output
    financial_analysis = []
    #  Each row is read as a row
    for row in csvreader:
        total_revenue = total_revenue + int(row[1])
        if first_record == "y":
            previous_month == row[0]
            previous_revenue = int(row[1])
            date_lst.append(row[0])
            revenue_lst.append(int(row[1]))
            first_record = "n"
        else:
            date_lst.append(row[0])
            revenue_lst.append(int(row[1]))
            month_revenue = previous_revenue - (int(row[1]))
            total_change_in_revenue = total_change_in_revenue + month_revenue
            previous_revenue = int(row[1])
          
    #  Total Months
    total_months = len(date_lst)

    #  Average Monthly Revenue Change
    avg_change = total_change_in_revenue//total_months
    
    #  Greatest Increase in Revenue
    max_revenue = max(revenue_lst)
    
    #  Least Increase in Revenue
    min_revenue = min(revenue_lst)
    
    # Index for Greatest Increase in Revenue
    max_keys = [i for i, x in enumerate(revenue_lst) if x == max_revenue]
    max_index = max_keys[0]
    max_dt = date_lst[max_index]
    # Index for Least Increase in Revenue
    min_keys = [i for i, x in enumerate(revenue_lst) if x == min_revenue]
    min_index = min_keys[0]
    min_dt = date_lst[min_index]
    
    print ("Financial Analysis")
    print ("------------------------------------------------")
    print ("Total Months:   " + str(total_months))
    print ("Total Revenue:  " + "$" + str(total_revenue))
    print ("Average Revenue Change:  "+ "$" + str(avg_change))
    print ("Greatest Increase in Revenue:  "+ str(max_dt) + "  ($" + str(max_revenue)+")")
    print ("Greatest Decrease in Revenue:  "+ str(min_dt) + "  ($" + str(min_revenue)+")")    

    financial_analysis.append("Total Months:   " + str(total_months))
    financial_analysis.append("Total Revenue:  " + "$" + str(total_revenue))
    financial_analysis.append("Average Revenue Change:  "+ "$" + str(avg_change))
    financial_analysis.append("Greatest Increase in Revenue:  "+ str(max_dt) + "  ($" + str(max_revenue)+")")
    financial_analysis.append("Greatest Decrease in Revenue:  "+ str(min_dt) + "  ($" + str(min_revenue)+")")
    
    with open(output_path, 'w', newline='') as csvfile:
         # Initialize csv.writer
         csvwriter = csv.writer(csvfile, delimiter=',')

         # Write the first row (column headers)
         csvwriter.writerow(['Financial Analysis'])

         # Write the rows
         csvwriter.writerows(financial_analysis)
         

