import os

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

    print("\nTotal number of files in the current directory: {}".format(file_count))
    print("\nFile Extensions and Counts:")
    print("+------------+-------+")
    print("| Extension  | Count |")
    print("+------------+-------+")
    for ext, count in extensions_count.items():
        print("| {:<10} | {:>5} |".format(ext, count))
    print("+------------+-------+")

    return extensions_count

def modify_category(extensions_count):
    print("\nSelect a category to modify:")
    print("0. All formats")
    for index, (ext, _) in enumerate(extensions_count.items(), start=1):
        print("{}. {}".format(index, ext))
    print("{}. All picture formats".format(len(extensions_count) + 1))

    try:
        choice = int(input("Enter the number of the category: "))
        if choice == 0:
            selected_category = "all"
            print("\nModifying category: {}".format(selected_category))
        elif choice <= len(extensions_count):
            selected_category = list(extensions_count.keys())[choice - 1]
            print("\nModifying category: {}".format(selected_category))
        else:
            selected_category = "pictures"
            print("\nModifying category: {}".format(selected_category))

        avoid_file = input("\nEnter the name of the file to avoid or press Enter to continue: ")
        avoid_file = avoid_file.lower()

        count = 1
        print("\nRenaming Files:")
        for file in os.listdir():
            if os.path.isfile(file) and file.lower() != avoid_file:
                _, extension = os.path.splitext(file)
                extension = extension.lower()
                if selected_category == "all" or (selected_category == "pictures" and extension in {".jpg", ".jpeg", ".png", ".gif", ".bmp"}):
                    new_name = "{}{}".format(count, extension)
                    os.rename(file, new_name)
                    print("| {:<30} | {:<30} |".format(file, new_name))
                    count += 1

        print("\nFiles renamed successfully!")
    except (ValueError, IndexError):
        print("\nInvalid choice. Please enter a valid number.")

if __name__ == "__main__":
    extensions_count = list_files()
    modify_category(extensions_count)
