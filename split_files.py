import csv
import sys
import os

def split_csv(input_file, num_files):
    with open(input_file, 'r') as file:
        # Read the CSV file
        reader = csv.reader(file)
        data = list(reader)

    # Calculate the number of rows in each split
    rows_per_split = len(data) // num_files

    # Split the data into specified number of files
    for i in range(num_files):
        start_index = i * rows_per_split
        end_index = (i + 1) * rows_per_split if i < num_files - 1 else len(data)
        split_data = data[start_index:end_index]

        # Generate output file name (1-based index)
        output_file = f"{input_file}_{i + 1}.csv"

        # Write the split data to the output file
        with open(output_file, 'w', newline='') as split_file:
            writer = csv.writer(split_file)
            writer.writerows(split_data)

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python script.py input_file num_files")
        sys.exit(1)

    # Get the input file name and number of files from the command-line arguments
    input_file = sys.argv[1]
    num_files = int(sys.argv[2])

    # Call the function with the provided input file and number of files
    split_csv(input_file, num_files)
