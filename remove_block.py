import sys

def remove_if_block(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    inside_block = False
    new_lines = []
    for line in lines:
        if 'if (shouldShrinkResources(project)) {' in line:
            inside_block = True
            continue
        elif inside_block and '}' in line:
            inside_block = False
            continue
        elif not inside_block:
            new_lines.append(line)

    with open(file_path, 'w') as file:
        file.writelines(new_lines)

if len(sys.argv) != 2:
    print("Usage: python remove_block.py <path_to_flutter_groovy>")
    sys.exit(1)

remove_if_block(sys.argv[1])
