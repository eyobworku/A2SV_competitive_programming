#!/bin/bash

# Check if a directory is provided as an argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <directory>"
    exit 1
fi

# Check if the provided directory exists
if [ ! -d "$1" ]; then
    echo "Error: Directory '$1' does not exist."
    exit 1
fi

# Move to the provided directory
cd "$1" || exit

# Iterate over all files in the directory
for file in *; do
    # Check if the file name contains spaces
    if [[ "$file" == *" "* ]]; then
        # Replace spaces with underscores
        new_file_name=$(echo "$file" | tr ' ' '_')

        # Rename the file
        mv "$file" "$new_file_name"
        
        # Output the renaming process
        echo "Renamed '$file' to '$new_file_name'"
    fi
done

echo "All files have been renamed."
