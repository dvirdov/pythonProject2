import os
import sys
import zipfile
import shutil


def unzip_and_get_working_directory(dir_name: str, zip_file: str) -> str:

    try:
        with zipfile.ZipFile(os.path.join(dir_name, zip_file), 'r') as zip_ref:
            zip_ref.extractall(dir_name)
        #shutil.rmtree(os.path.join(dir_name, zip_file))
        os.remove(os.path.join(dir_name, zip_file))
    except zipfile.BadZipfile as error:
        print(dir_name)


def fixed_name(name: str):
    new_name = ""
    for letter in name:
        if is_good_char(letter):
            new_name += letter
    return new_name


def is_good_char(letter:str):
    try:
        letter.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return letter == '.'
    else:
        return False
    # return letter.isdigit()


def set_directory_content_to_suitable_names(dir_name:str):
    only_files = [f for f in os.listdir(dir_name)]

    for filename in only_files:
        name_without_extension, extension = os.path.splitext(filename)
        new_name = fixed_name(name_without_extension)
        os.rename(os.path.join(dir_name, filename), os.path.join(dir_name, new_name + extension))


def rename_file(dir_path, old_name, new_name):
    _, extension = os.path.splitext(old_name)
    os.rename(os.path.join(dir_path, old_name), os.path.join(dir_path, new_name + extension))


def main():
    working_dir = sys.argv[1]
    set_directory_content_to_suitable_names(working_dir)
    # for dirname in [f for f in os.listdir(working_dir)]:
    #     # set_directory_content_to_numeric_names(os.path.join(working_dir, filename))
    #     for filename in os.listdir(os.path.join(working_dir, dirname)):
    #         rename_file(os.path.join(working_dir, dirname), filename, dirname)
    #     for filename in os.listdir(os.path.join(working_dir, dirname)):
    #         unzip_and_get_working_directory(os.path.join(working_dir, dirname), filename)


if __name__ == '__main__':
    main()
