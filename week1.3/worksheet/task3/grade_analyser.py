# Worksheet 1.3: Task 3

# Your code for the overall grade classification

# ask for filename of the student file

# open the file

# read in the data, and for each student calculate their average grade and classification



# write out this calculated data in the format without a header:
#      student_id,average_grade,classification - replace this with actual value
#      The average grade should be given to 2 decimal places
#      this can be achieved by using the following in an fstring: {variable_name:.2f}


# write this data out to a file named input_file_name + _out.csv - e.g. the input file name 'student_data.csv' -> 'student_data.csv_out.csv'

# You can compare your output files with the 4 example files in example_outfiles folder




import os


script_folder = os.path.dirname(os.path.abspath(__file__))

input_filename = input("Enter the student file name: ")


if not input_filename.endswith('.csv'):
    input_filename = input_filename + '.csv'

input_file_path = os.path.join(script_folder, input_filename)
output_file_path = os.path.join(script_folder, f"{input_filename}_out.csv")

with open(input_file_path, 'r') as infile, open(output_file_path, 'w') as outfile:
    next(infile)
    
    for line in infile:
        line = line.strip()
        if not line:
            continue
        
        parts = line.split(',')
        student_id = parts[0]
        
        grades = []
        for grade_str in parts[1:]:
            if grade_str.strip() != '':
                grades.append(int(grade_str))
        
        average = sum(grades) / len(grades)
        
        if average >= 70:
            classification = "1"
        elif average >= 60:
            classification = "2:1"
        elif average >= 50:
            classification = "2:2"
        elif average >= 40:
            classification = "3"
        else:
            classification = "F"
        
        outfile.write(f"{student_id},{average:.2f},{classification}\n")