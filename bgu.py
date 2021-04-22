import os
import sys


def is_foreign_letter(letter: str):
    try:
        letter.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return True  # cant be coded into ascii - means foreign letter
    else:
        return False


def alternate_name_in_hebrew(name: str):
    new_name = ""
    for letter in name:
        if is_foreign_letter(letter) or letter == ' ':
            new_name += letter
    return new_name


def name_contains_id(name: str):
    number_of_digits = 0
    for letter in name:
        if letter.isdigit():
            number_of_digits += 1
    return number_of_digits >= 8


def set_directory_content_to_suitable_names(dir_name:str):
    for folder_name in os.listdir(dir_name):
        full_folder_name = os.path.join(dir_name, folder_name)
        for zip_file_name in os.listdir(full_folder_name):
            new_name, _ = os.path.splitext(zip_file_name)
            if not name_contains_id(new_name):
                new_name = alternate_name_in_hebrew(folder_name)
            new_full_name = os.path.join(dir_name, new_name)
            os.rename(full_folder_name, new_full_name)


def main():
    working_dir = sys.argv[1]
    set_directory_content_to_suitable_names(working_dir)


if __name__ == '__main__':
    main()
