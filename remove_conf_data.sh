#!/bin/bash

# Check if the user has provided a directory as an argument
if [ "$#" -ne 1 ]; then
    echo "Usage: ./remove_confidence_scores.sh <directory_path>"
    exit 1
fi

# Function to process each file
process_file() {
    local file="$1"
    echo "Processing $file"
    # Use sed to remove all lines from 'Confidence Scores % (Table Cell)' and below
    sed -e '/Confidence Scores % (Table Cell)/,$d' "$file" > "temp_file.csv"
    # Move the temp file back to the original file
    mv "temp_file.csv" "$file"
}

# Get the directory path
directory_path="$1"

# Find all CSV files in directory and subdirectories and process each file
find "$directory_path" -type f -name '*.csv' -print0 | while IFS= read -r -d '' file; do
    process_file "$file"
done

echo "All files processed successfully."
