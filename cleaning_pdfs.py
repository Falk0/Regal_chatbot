import re
import pandas as pd
import os
import sys


def clean_text(text):
    # Remove special characters
    text = re.sub(r'[^\w\s]', '', text)
    # Replace multiple spaces with a single space
    text = re.sub(r'\s+', ' ', text)
    # Remove leading and trailing whitespace
    text = text.strip()
    return text

def read_csv_files_from_directory(directory_path):
    dataframes = []
    
    # List all files in directory
    try:
        files = os.listdir(directory_path)
    except FileNotFoundError:
        print(f"The directory {directory_path} does not exist.")
        return dataframes
    
    # Loop through each file
    for file in files:
        if file.endswith('.csv'):
            # Construct full file path
            file_path = os.path.join(directory_path, file)
            # Read CSV file into a DataFrame
            try:
                df = pd.read_csv(file_path)
                df = df.dropna(axis=1, how='all')

                if should_transpose(df):
                    # Transpose the DataFrame
                    transposed_df = df.transpose()

                    # Use the first row as the columns headers
                    transposed_df.columns = transposed_df.iloc[0]

                    # Drop the first row as it's now the header
                    df = transposed_df.drop(transposed_df.index[0])
                # Append DataFrame to the list
                dataframes.append(df)
                print(f"Successfully read {file_path}")
            except Exception as e:
                print(f"Could not read {file_path} - {str(e)}")
    
    return dataframes

def should_transpose(df):
    # Check if DataFrame has only two columns
    if df.shape[1] != 2:
        return False
    else:
        return True
    

path = ''

dataframes = read_csv_files_from_directory(path)
for i in range(len(dataframes)):
    output_file = f'/path/data{i}.csv'
    df = dataframes[i]
    print(df)
    df.to_csv(output_file)

