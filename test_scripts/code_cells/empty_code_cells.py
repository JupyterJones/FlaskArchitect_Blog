!pwd

import os
import logging
import nbformat

def search_in_ipynb(directory, term):
    # Configure logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    # Walk through the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".ipynb"):
                file_path = os.path.join(root, file)
                
                # Read the Jupyter notebook
                with open(file_path, "r", encoding="utf-8") as nb_file:
                    try:
                        notebook = nbformat.read(nb_file, as_version=4)
                        
                        # Search for the term in cells
                        for cell_num, cell in enumerate(notebook['cells']):
                            if 'source' in cell and term in cell['source']:
                                logger.info(f"Found in {file_path}, cell {cell_num + 1}")

                                # Display 5 lines before the term
                                start_line = max(cell['source'].count('\n', 0, cell['source'].index(term)) - 4, 0)
                                before_lines = cell['source'].split('\n')[start_line:start_line + 5]
                                for line_num, line in enumerate(before_lines):
                                    logger.info(f"  {start_line + line_num + 1}: {line}")

                                # Display the line with the term
                                logger.info(f"  {start_line + len(before_lines) + 1}: {cell['source'].split(term)[0]}{term}")

                                # Display 5 lines after the term
                                after_lines = cell['source'].split(term)[1].split('\n')[:5]
                                for line_num, line in enumerate(after_lines):
                                    logger.info(f"  {start_line + len(before_lines) + 2 + line_num}: {line}")

                    except Exception as e:
                        logger.error(f"Error reading {file_path}: {e}")

if __name__ == "__main__":
    # Replace 'your_directory_path' with the actual directory path you want to search
    search_directory = '/mnt/HDD500/notebooks'
    
    # Replace 'your_search_term' with the term you want to search for
    search_term = 'quantum'

    search_in_ipynb(search_directory, search_term)


import os
import logging

def search_in_txt(directory, term):
    # Configure logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    # Walk through the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".ipynb"):
                file_path = os.path.join(root, file)

                # Read the text file
                with open(file_path, "r", encoding="utf-8") as txt_file:
                    try:
                        lines = txt_file.readlines()

                        # Search for the term in each line
                        for line_num, line in enumerate(lines):
                            if term in line:
                                logger.info(f"Found in {file_path}, line {line_num + 1}")

                                # Display 5 lines before the term
                                start_line = max(line_num - 4, 0)
                                before_lines = lines[start_line:line_num]
                                for ln, l in enumerate(before_lines):
                                    logger.info(f"  {start_line + ln + 1}: {l.strip()}")

                                # Display the line with the term
                                logger.info(f"  {line_num + 1}: {line.strip()}")

                                # Display 5 lines after the term
                                after_lines = lines[line_num + 1:line_num + 6]
                                for ln, l in enumerate(after_lines):
                                    logger.info(f"  {line_num + 2 + ln}: {l.strip()}")

                    except Exception as e:
                        logger.error(f"Error reading {file_path}: {e}")

if __name__ == "__main__":
    # Replace 'your_directory_path' with the actual directory path you want to search
    search_directory = '/mnt/HDD500/notebooks'
    
    # Replace 'your_search_term' with the term you want to search for
    search_term = 'bash'

    search_in_txt(search_directory, search_term)


#!/bin/bash

# Replace 'your_directory_path' with the actual directory path you want to search
search_directory='/home/jack/Documents/CHATDPT'

# Replace 'your_search_term' with the term you want to search for
search_term='search_term'

# Use find to locate all .txt files in the specified directory
find "$search_directory" -type f -name "*.json" -print0 |
while IFS= read -r -d '' file; do
    # Use grep to search for the term in the file
    grep -n -A 5 -B 5 "$search_term" "$file" |
    # Use awk to format and print the results
    awk -v file="$file" '{printf "Found in %s, %s\n", file, $0}'
done


#!/bin/bash

# Replace 'your_directory_path' with the actual directory path you want to search
search_directory='/home/jack/Documents/CHATDPT'

# Replace 'your_search_term' with the term you want to search for
search_term='search_term'

# Use find to locate all .txt files in the specified directory
find "$search_directory" -type f -name "*.json" -print0 |
while IFS= read -r -d '' file; do
    # Use grep to search for the term in the file
    grep -n -A 5 -B 5 "$search_term" "$file" |
    # Use awk to format and print the results
    awk -v file="$file" '{printf "Found in %s, %s\n", file, $0}' >> SEARCH.txt
done


#!/bin/bash

# Replace 'your_directory_path' with the actual directory path you want to search
search_directory='/home/jack/Documents/CHATDPT'

# Replace 'your_search_term' with the term you want to search for
search_term='search_term'

# Use find to locate all .txt files in the specified directory
find "$search_directory" -type f -name "*.json" -print0 |
while IFS= read -r -d '' file; do
    # Use grep to search for the term in the file
    grep -n -A 5 -B 5 "$search_term" "$file" |
    # Use awk to format and print the results
    awk -v file="$file" '{printf "Found in %s, %s\n", file, $0}' >> SEARCH.txt
    # Add a newline after each file's results
    echo >> SEARCH.txt
done


#!/bin/bash

# Replace 'your_directory_path' with the actual directory path you want to search
search_directory='/home/jack/Documents/CHATDPT'

# Replace 'your_search_term' with the term you want to search for
search_term='search_term'

# Use find to locate all .txt files in the specified directory
find "$search_directory" -type f -name "*.json" -print0 |
while IFS= read -r -d '' file; do
    # Use grep to search for the term in the file
    grep -n -A 5 -B 5 "$search_term" "$file" |
    # Use awk to format and print the results, replacing \n with actual newline
    awk -v file="$file" '{gsub(/\\n/, "\n"); printf "Found in %s, %s\n", file, $0}' >> SEARCH.txt
    # Add a newline after each file's results
    echo >> SEARCH.txt
done


import os

# Replace 'your_directory_path' with the actual directory path you want to search
search_directory = '/home/jack/Documents/CHATDPT'

# Replace 'your_search_term' with the term you want to search for
search_term = 'search_term'

# Output file
output_file = 'SEARCH_json.txt'

with open(output_file, 'w') as output:
    # Walk through the directory
    for root, dirs, files in os.walk(search_directory):
        for file in files:
            if file.endswith(".json"):
                file_path = os.path.join(root, file)
                
                # Read the text file
                try:
                    with open(file_path, 'r', encoding='utf-8') as txt_file:
                        lines = txt_file.readlines()
                        
                        # Search for the term in the text file
                        for line_num, line in enumerate(lines):
                            if search_term in line:
                                output.write(f"Found in {file_path}, line {line_num + 1}\n")

                                # Display 5 lines before and after the term
                                start_line = max(line_num - 5, 0)
                                for i in range(start_line, min(len(lines), line_num + 6)):
                                    output.write(f"  {i + 1}: {lines[i]}")

                                output.write("------------------\n")

                except Exception as e:
                    print(f"Error reading {file_path}: {e}")

print("Search results saved to", output_file)


!ls SEARCH_json.txt



