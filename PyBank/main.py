import csv  
import os  


cwd = os.getcwd()  # Get the current working directory (cwd)

# get the file path
file1 = cwd + os.path.join("\\python-challenge","PyBank","Resources", "budget_data.csv")

# create list to store data
budget_data = []

with open(file1) as csv_file:
    reader = csv.DictReader(csv_file)

    # looping through data to store in dictionary. We are all adding the definitions into a list (budget_data)
    for row in reader:
        budget_data.append(
            {"month": row["Date"], "amount": int(row["Profit/Losses"]), "change": 0}
        )

# calculate the total months. Using the len function to count objects in data set
total_months = len(budget_data)

# print(total_months)
# looping the dictionary so we can calculate the changes between the months
prev_amount = budget_data[0]["amount"]
for i in range(total_months):
    budget_data[i]["change"] = budget_data[i]["amount"] - prev_amount
    prev_amount = budget_data[i]["amount"]

# calculate total amount
total_amount = sum(row["amount"] for row in budget_data)

# average change
# sum all of rows of change/total months
total_row_change = sum(row["change"] for row in budget_data)
average = round(total_row_change / (total_months - 1), 2)


great_increase = max(budget_data, key=lambda x: x["change"])

great_decrease = min(budget_data, key=lambda x: x["change"])

# we use lambda to sort information we need. In this case we need the change and amount. Using the lambda function gives us what we're looking for

# Print all the info we have gathered
Final_Report = [
    ("PyBank Analysis"),
    (f"Total Months: {total_months}"),
    (f"Total: {total_amount}"),
    (f"Average Change: {average}"),
    (
        f'Greatest Increase in Profits: {great_increase["month"]} ${great_increase["change"]}'
    ),
    (
        f'Greatest Decrease in Profits: {great_decrease["month"]} ${great_decrease["change"]}'
    ),
]
print(Final_Report)


# transfer everything to a text file
# print must include file=*conversion*
# "w" must be included to write
# formatting became a little janky when trying to print (final_report) onto text_file. Wrote it out for clear understanding
file2 = cwd + os.path.join("\\python-challenge","PyBank","Analysis", "pyBankAnalysis.txt")

with open(file2, "w") as text_file:
    print("PyBank Analysis", file=text_file)
    print("----------------------", file=text_file)
    print(f"Total Months: {total_months}", file=text_file)
    print(f"Total: {total_amount}", file=text_file)
    print(f"Average Change: {average}", file=text_file)
    print(
        f'Greatest Increase in Profits: {great_increase["month"]} ${great_increase["change"]}',
        file=text_file,
    )
    print(
        f'Greatest Decrease in Profits: {great_decrease["month"]} ${great_decrease["change"]}',
        file=text_file,
    )
