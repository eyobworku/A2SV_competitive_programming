#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <folder_path> <text_file>"
    exit 1
fi

# Check if the provided folder exists
if [ ! -d "$1" ]; then
    echo "Error: Directory '$1' does not exist."
    exit 1
fi

# Check if the provided text file exists
if [ ! -f "$2" ]; then
    echo "Error: File '$2' does not exist."
    exit 1
fi

# Read each string from the text file and create a Python file with modified filenames
while IFS= read -r line; do
    # Replace spaces with underscores
    new_filename=$(echo "$line" | tr ' ' '_')

    # Create a Python file with the modified filename
    touch "$1/$new_filename.py"

    echo "Created file: $new_filename.py"
done < "$2"

echo "Python files have been created in the folder: $1"
