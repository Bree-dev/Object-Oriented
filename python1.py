# File Read & Write Challenge with Error Handling

def modify_content(content):
    # Example modification: Convert text to uppercase
    return content.upper()

def main():
    input_filename = input("Enter the filename to read: ")

    try:
        # Try to open and read the input file
        with open(input_filename, 'r') as infile:
            content = infile.read()
        
        # Modify the content
        modified_content = modify_content(content)

        # Define a new output filename
        output_filename = "modified_" + input_filename

        # Write the modified content to the new file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"Modified content written to '{output_filename}' successfully.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: Could not read from or write to file '{input_filename}'.")

if __name__ == "__main__":
    main()
