
# Join the contents of the three files with the dots and spaces into a single file
# cat lactea_points.txt andromeda_points.txt cartwheel_points.txt > joined_points.txt
#
# cat lactea_points.txt cartwheel_points.txt andromeda_points.txt > joined_points.txt

# Open the file and read the text
with open("joined_points.txt", "r") as open_file:
    text = open_file.read()

# Convert spaces to 0 and dots to 1
def convert_to_binary(text):
    binary_text = ""
    for char in text:
        if char == " ":
            binary_text += "0"
        elif char == ".":
            binary_text += "1"
    return binary_text


# Convert the text to binary
binary_text = convert_to_binary(text)
char = ""
for i in range(0, len(binary_text), 8):
    char += chr(int(binary_text[i:i+8], 2))

# write the binary text to a file
write_file = open("../secrets/output_final_points.json", "w")
write_file.write(char)
write_file.close()