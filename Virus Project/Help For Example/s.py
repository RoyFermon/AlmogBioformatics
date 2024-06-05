def replace_letters_in_place(file_path):
    # Define the replacement rules
    replacement_rules = {
        'A': 'T',
        'T': 'C',
        'C': 'G',
        'G': 'A'
    }

    try:
        # Read the input file
        with open(file_path, 'r') as file:
            content = file.read()

        # Perform the replacements
        replaced_content = ''.join([replacement_rules.get(char, char) for char in content])

        # Write the modified content back to the same file
        with open(file_path, 'w') as file:
            file.write(replaced_content)

        print(f"Replacements complete. Modified content saved to {file_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Usage
file_path = 'BadLettuce.fasta'  # Replace with your file path
replace_letters_in_place(file_path)
