#!/bin/bash

# Check if a folder path is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <folder_path>"
  exit 1
fi

# Check if the provided folder exists
if [ ! -d "$1" ]; then
  echo "Error: Folder not found: $1"
  exit 1
fi

# Set the folder path and the output file
folder_path=$(realpath "$1")
output_file="${folder_path}/_md5_results.txt"

# Remove the output file if it exists
if [ -f "$output_file" ]; then
  rm "$output_file"
fi

# Iterate over the files in the folder and calculate their MD5 hashes, excluding hidden files and _md5_results.txt
find "$folder_path" -type f ! -name ".*" ! -name "_md5_results.txt" -exec sh -c 'md5 -q "{}" | { read -a arr; echo "${arr[0]} $(basename "{}")"; }' \; >> "$output_file"

# Print the output file path
echo "MD5 hashes stored in: $output_file"
