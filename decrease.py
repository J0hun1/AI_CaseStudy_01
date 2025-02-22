import pandas as pd

def decrease_column_values(file_path, column_name):
    # Read the CSV file
    df = pd.read_csv(file_path)
    
    # Decrease the values in the specified column by 10% and round to 1 decimal place
    df[column_name] = (df[column_name] * 0.9).round(1)
    
    # Write the updated DataFrame back to the CSV file
    df.to_csv(file_path, index=False)

# Example usage
file_path = 'data/V5_student_sleep_patterns.csv'
column_name = 'Physical_Activity'
decrease_column_values(file_path, column_name)