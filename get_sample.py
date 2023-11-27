import csv
import sys
import os

def extract_and_save_first_10(input_file):
    with open(input_file, 'r') as file:
        # Read the CSV file
        reader = csv.reader(file)
        data = [next(reader) for _ in range(10)]  # Extract the first 10 rows

    # Generate output file name
    output_file = f"{os.path.splitext(input_file)[0]}_test.csv"

    # Write the extracted data to the output file
    with open(output_file, 'w', newline='') as test_file:
        writer = csv.writer(test_file)
        writer.writerows(data)

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python script.py input_file")
        sys.exit(1)

    # Get the input file name from the command-line arguments
    input_file = sys.argv[1]

    # Call the function with the provided input file
    extract_and_save_first_10(input_file)
