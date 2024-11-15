import sys

def remove_code_blocks(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    inside_block = False
    bracket_counter = 0
    new_lines = []
    for line in lines:
        # Check if the line starts the if block
        if 'if (shouldShrinkResources(project)) {' in line:
            inside_block = True
            bracket_counter = 1  # Start counting from 1 because we have one opening bracket
            continue
        # Check if the line starts the method block
        elif 'private static Boolean shouldShrinkResources(Project project) {' in line:
            inside_block = True
            bracket_counter = 1  # Start counting from 1 because we have one opening bracket
            continue
        elif inside_block:
            open_brackets = line.count('{')
            close_brackets = line.count('}')
            bracket_counter += open_brackets
            bracket_counter -= close_brackets
            if bracket_counter > 0:
                continue
            else:
                inside_block = False
        elif not inside_block:
            new_lines.append(line)

    # Write the modified content back to the file
    with open(file_path, 'w') as file:
        file.writelines(new_lines)

if len(sys.argv) != 2:
    print("Usage: python remove_block.py <path_to_file>")
    sys.exit(1)

remove_code_blocks(sys.argv[1])
