import os
from colorama import Fore, Style

# Install colorama if not installed yet
# pip install colorama

def list_files():
    file_count = 0
    extensions_count = {}

    for file in os.listdir():
        if os.path.isfile(file):
            file_count += 1
            _, extension = os.path.splitext(file)
            extension = extension.lower()
            if extension in extensions_count:
                extensions_count[extension] += 1
            else:
                extensions_count[extension] = 1

    print("\n" + Fore.GREEN + "Total number of files in the current directory: {}".format(file_count) + Style.RESET_ALL)
    print("\n" + Fore.YELLOW + "File Extensions and Counts:" + Style.RESET_ALL)
    print(Fore.CYAN + "+------------+-------+")
    print("| Extension  | Count |")
    print("+------------+-------+")
    for ext, count in extensions_count.items():
        print("| {:<10} | {:>5} |".format(ext, count))
    print("+------------+-------+" + Style.RESET_ALL)

    return extensions_count

def modify_category(extensions_count):
    print("\n" + Fore.YELLOW + "Select a category to modify:" + Style.RESET_ALL)
    for index, (ext, _) in enumerate(extensions_count.items(), start=1):
        print("{}. {}".format(index, ext))

    try:
        choice = int(input("Enter the number of the category: "))
        selected_category = list(extensions_count.keys())[choice - 1]
        print("\nModifying category: {}{}".format(Fore.CYAN, selected_category) + Style.RESET_ALL)

        avoid_file = input("\nEnter the name of the file to avoid or press Enter to continue: ")
        avoid_file = avoid_file.lower()

        count = 1
        print("\n" + Fore.YELLOW + "Renaming Files:" + Style.RESET_ALL)
        print(Fore.CYAN + "+-------------------------------+-------------------------------+")
        print("| {:<30} | {:<30} |".format("Original Name", "New Name"))
        print("+-------------------------------+-------------------------------+" + Style.RESET_ALL)
        for file in os.listdir():
            if os.path.isfile(file) and file.lower() != avoid_file:
                _, extension = os.path.splitext(file)
                extension = extension.lower()
                if extension == selected_category:
                    new_name = "{}{}".format(count, extension)
                    os.rename(file, new_name)
                    print("| {:<30} | {:<30} |".format(file, new_name))
                    count += 1

        print("\n" + Fore.GREEN + "Files renamed successfully!" + Style.RESET_ALL)
    except (ValueError, IndexError):
        print("\n" + Fore.RED + "Invalid choice. Please enter a valid number." + Style.RESET_ALL)

if __name__ == "__main__":
    extensions_count = list_files()
    modify_category(extensions_count)