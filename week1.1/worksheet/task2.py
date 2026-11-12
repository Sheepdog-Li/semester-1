"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: 
"""

name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")


month_saving = input("How much you want to save every month:")

if not month_saving.isdigit():
    print("Invalid amount")
    exit()

number = int(month_saving)
year_saving = number * 12
year_saving = int(year_saving)
print(f"you are going to save {year_saving} in this year.")

    
total_saving = year_saving + year_saving * 0.008
total_saving = float(total_saving)
print(f"you will have £{total_saving:.2f} in this year")
    


# Ask the user to input an amount they want to save every month - this should be an integer.
# Validate that they have entered an integer.


# Calculate the total amount of money they will have saved by the end of the year (amount per month multiplied by 12).
# print this out for the user with a suitable message.


# Calculate the total amount of money including interest (0.8% of the final annual amount) they will have saved in a year.
# print this out in the format £X.XX (to two decimal places).

