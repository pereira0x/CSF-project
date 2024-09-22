# Define the input and output file paths
input_filename = "throne.txt"
output_filename = "wordlist.txt"

# Read the input data from the file
with open(input_filename, "r") as file:
    input_data = file.read()

# Split the input data by any whitespace (spaces, newlines, tabs, etc.)
words = input_data.split()

# Write each word on a new line in the output file
with open(output_filename, "w") as file:
    for word in words:
        file.write(word + "\n")

print(f"Output file '{output_filename}' has been created with {len(words)} words.")
