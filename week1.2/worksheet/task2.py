# Worksheet 1.2: Task 2 Solution



import sys
from util import read_numbers

num_list = read_numbers()

if len(num_list) == 0:
    sys.exit("Error: no numbers provided")

min_value = min(num_list)
max_value = max(num_list)
mean_value = sum(num_list) / len(num_list)

print(f"Minimum = {min_value}")
print(f"Maximum = {max_value}")
print(f"Mean = {mean_value}")

sorted_num = sorted(num_list)
n = len(sorted_num)

if n % 2 == 1:
    mediannum_odd = n // 2
    mediannum_final = sorted_num[mediannum_odd]
else:
    evennum1 = (n // 2) - 1
    evennum2 = n // 2
    mediannum_final = (sorted_num[evennum1] + sorted_num[evennum2]) / 2

print(f"Median = {mediannum_final}")






