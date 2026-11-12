# Worksheet 1.2: Task 1 Solution



import sys

grade = input("enter an integer grade in the range 0 to 100:")


if not grade.isdecimal():
    sys.exit("Error: Grade must be an integer between 0 and 100")

grade = int(grade)

if grade > 100 or grade < 0:
    sys.exit("Error: Grade must be an integer between 0 and 100")


if 0 <= grade <= 39 :
    print(f"{grade} is a Fail")
elif 40 <= grade <= 69 :
    print(f"{grade} is a Pass")
elif 70 <= grade <= 100:
    print(f"{grade} is a Distinction")
else:
    print("Error: Grade must be an integer between 0 and 100")



