#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <folder_path> <output_text_file>"
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

# URL prefix
url_prefix="https://github.com/eyobworku/A2SV_competitive_programming/blob/main/$1"

# Append each file name to the URL prefix and append it to the text file
#for file in "$1"/*; do
find "$1" -type f -mtime -1 -print0 | while IFS= read -r -d '' file; do
    # Get the file name without the path
    file_name=$(basename "$file")

    # Append the file name to the URL prefix
    url="$url_prefix$file_name"

    # Append the URL to the text file
    echo "$url" >> "$2"

    echo "Appended URL: $url"
done

echo "URLs have been appended to the text file: $2"
