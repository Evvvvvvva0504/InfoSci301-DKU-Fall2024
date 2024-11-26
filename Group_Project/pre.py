import pandas as pd
import csv


def preprocess_csv(input_file, output_file):
    try:
        # Open the input file with a specified encoding
        with open(input_file, 'r', encoding='latin1') as infile:
            reader = csv.reader(infile)
            rows = []
            
            # Collect valid rows
            for row in reader:
                rows.append(row)  # Append each valid row to the list

        # Write the cleaned data into a new CSV file
        with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile)
            writer.writerows(rows)

        print(f"Preprocessed file saved as: {output_file}")
    except Exception as e:
        print(f"An error occurred during preprocessing: {e}")

def select_rows(file_path, output_file_first, output_file_random):
    # Load the large dataset
    df = pd.read_csv(file_path)
    
    # Select the first 20000 rows and save to a new file
    df_first_20000 = df.head(20000)
    df_first_20000.to_csv(output_file_first, index=False)

    # Randomly select 20000 rows and save to another file
    df_random_20000 = df.sample(n=20000, random_state=42)
    df_random_20000.to_csv(output_file_random, index=False)

    print(f"First 20000 rows saved to: {output_file_first}")
    print(f"Random 20000 rows saved to: {output_file_random}")

if __name__ == "__main__":
    input_file = 'Dataset/absentee_20241105.csv'  # Replace with the path to your input file
    output_file = 'Dataset/absentee_20241105_preprocessed.csv'  # Replace with your desired output file path
    # preprocess_csv(input_file, output_file)
    data = pd.read_csv('Dataset/absentee_20241105_preprocessed.csv')
    file_path = 'Dataset/absentee_20241105_preprocessed.csv'
    output_file_first_20000 = 'Dataset/absentee_first_20000.csv'
    output_file_random_20000 = 'Dataset/absentee_random_20000.csv'

    select_rows(file_path, output_file_first_20000, output_file_random_20000)   

