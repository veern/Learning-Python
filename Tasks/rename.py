import os

def find_all(file: str, path: str) -> str:
    for root, dirs, files in os.walk(path):
        if file in files:
            yield os.path.join(root, file)
        elif dirs in files:
            yield os.path.join(root, dirs)

def print_files_in_dir(files: list[str], path: str) -> None:
    print(f"Files inside of: {path}\n")
    for file in files:
        print(file)

def welcome() -> None:
    os.system("cls")
    print("Welcome to multi functional tool!")

def bulk_single_find() -> None:
    choice = 0
    try:
        choice = int(input("\nChoose mode of the tool:\n1. bulk rename\n2. single file rename\n3. find files (with extension)\n(type the number associated): "))
    except ValueError:
        bulk_single_find()
    if choice == 3:
        file = input("\nFile to search: ")
        for f in find_all(file, "C:\\"):
            print(f)
        exit()
    if choice == 1: return bulk_file_rename(dir_check())
    elif choice == 2: return single_file_rename(dir_check())
    else: bulk_single_find()

def dir_check() -> str:
    path_input = input("Enter the path of a directory that contains the files you would like to rename: ")
    while not os.path.isdir(path_input):
        path_input = input("Path is not valid! Enter the path of a directory that contains file that you would like to rename!: ")
    print_files_in_dir(os.listdir(path_input), path_input)
    return path_input

def single_file_rename(path_input: str) -> None:
    file_input = input("Write down a name of the file in the specified directory: ")
    while not os.path.isfile(f"{path_input}\{file_input}"):
        file_input = input("Write a correct name of a file found in specified directory: ")
    extension = file_input.split(".")[1]
    file_new_name = input("Write down a new name for the file you have selected (no extension): ")
    while "." in file_new_name:
        file_new_name = input("Write down a correct new name for the file you have selected (no extension): ")
    os.rename(f"{path_input}\{file_input}", f"{path_input}\{file_new_name}.{extension}")
    exit()

def bulk_file_rename(path_input: str) -> None:
    files_new_name = input("\nWrite down a new name for the files: ")
    while "." in files_new_name:
        files_new_name = input("Write down a correct new name for the file you have selected (no extension): ")
    for id, file in enumerate(os.listdir(path_input)):
        extension = file.split(".")[1]
        os.rename(f"{path_input}\{file}", f"{path_input}\{files_new_name}_{id}.{extension}")
    exit()

def main():
    welcome()
    bulk_single_find()
    
if __name__ == "__main__":
    main()