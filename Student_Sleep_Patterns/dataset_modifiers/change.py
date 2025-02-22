import csv
import random

def change_other_to_gender(input_file, output_file, column_name):
    with open(input_file, mode='r', newline='') as infile, open(output_file, mode='w', newline='') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for row in reader:
            if row[column_name] == 'Other':
                row[column_name] = random.choice(['Male', 'Female'])
            writer.writerow(row)

input_file = 'data/V2_student_sleep_patterns.csv'
output_file = 'data/V3_student_sleep_patterns.csv'
column_name = 'Gender'
change_other_to_gender(input_file, output_file, column_name)