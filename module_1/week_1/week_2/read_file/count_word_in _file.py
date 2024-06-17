
def count_word(path):
    with open(path, "r") as file:
        contents = file.read()

    if len(contents) == 0:
        return None

    contents = contents.lower()
    contents = contents.split()

    return {content: contents.count(content) for content in contents}


list_path = ['P0_data.txt', 'P1_data.txt', 'P2_data.txt']
index = 1
for path in list_path:
    first_path = 'AIO_2024/module_1/week_2/read_file/test_data/'
    path = first_path + path

    output = count_word(path)
    print(f"output {index}: ", output if output !=
          None else "There is no content in the file")
    index += 1
    print()
