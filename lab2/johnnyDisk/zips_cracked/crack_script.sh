#!/bin/bash


# run the obuscator_reversed.py script first with the first argument first zip file name 77 times
for i in {1..71}; do
  python3 obfuscator_reversed.py 1727365201
done


# Loop over all zip files in the current directory
for zipfile in backup_*.zip; do
  # Extract the number part from the filename using parameter expansion
  number=$(echo "$zipfile" | sed -E 's/backup_([0-9]+)\.zip/\1/')
  
  # Run the obfuscator_reversed.py with the extracted number
  python3 obfuscator_reversed.py "$number"
  
  # Optional: print a message after running the script
  echo "Ran obfuscator_reversed.py with argument: $number"
done
