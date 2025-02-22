import csv

def modify_csv(input_file, output_file, target_column, compare_column, threshold):
    with open(input_file, mode='r', newline='') as infile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        rows = list(reader)

    for row in rows:
        if float(row[compare_column]) > threshold:
            row[target_column] = str(int(row[target_column]) + 0)
        elif float(row[compare_column]) == threshold:
            row[target_column] = str(int(row[target_column]) + 0)
        elif float(row[compare_column]) < threshold:
            row[target_column] = str(int(row[target_column]) - 1)

    with open(output_file, mode='w', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

if __name__ == "__main__":
    input_file = 'data/V6_student_sleep_patterns.csv'  # Replace with your input CSV file path
    output_file = 'data/V6_student_sleep_patterns.csv'  # Replace with your output CSV file path
    target_column = 'Sleep_Quality'  # Replace with the column you want to modify
    compare_column = 'Sleep_Duration'  # Replace with the column you want to compare the threshold with
    threshold = 4  # Replace with your threshold value

    modify_csv(input_file, output_file, target_column, compare_column, threshold)
