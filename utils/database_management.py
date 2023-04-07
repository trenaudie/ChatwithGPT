from config import Config


def read_file_list():
    filename = Config.file_list_path
    file_list = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            file_list.append(line.strip())

    return file_list


def write_to_file_list(filename):
    filepath = Config.file_list_path
    with open(filepath, 'a', encoding='utf-8') as file:
        file.write(filename + "\n")
