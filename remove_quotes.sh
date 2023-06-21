#!/bin/bash

# Check if provided directory
if [ "$#" -ne 1 ]; then
    echo "Usage: ./remove_quotes.sh <directory_path>"
    exit 1
fi

# Function to process each file, remove single and double quotes
process_file() {
    local file="$1"
    echo "Processing $file"
    sed -i.bak 's/["'\'']//g' "$file"
}

# Get the directory path
directory_path="$1"

# Find all CSV files in directory and subdirectories and process each file
find "$directory_path" -type f -name '*.csv' -print0 | while IFS= read -r -d '' file; do
    process_file "$file"
done

echo "All files processed successfully."
