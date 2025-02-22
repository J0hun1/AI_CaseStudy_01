import csv

def remove_columns(input_file, output_file, columns_to_remove):
    with open(input_file, 'r', newline='') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        headers = next(reader)
        indices_to_remove = [headers.index(col) for col in columns_to_remove if col in headers]

        writer.writerow([col for i, col in enumerate(headers) if i not in indices_to_remove])

        for row in reader:
            writer.writerow([col for i, col in enumerate(row) if i not in indices_to_remove])

if __name__ == "__main__":
    input_file = input("Enter the input CSV file path: ")
    output_file = input("Enter the output CSV file path: ")
    columns_to_remove = input("Enter the columns to remove (comma-separated): ").split(',')

    remove_columns(input_file, output_file, [col.strip() for col in columns_to_remove])