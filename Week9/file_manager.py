import os

def file_manager_demo():
    # new folder lab_files
    folder= "lab_files"

    # display working directory
    cwd = os.getcwd()
    print(f"Current working directory: {cwd}")

    # 3 empty text files inside folder
    if not os.path.exists(folder):
        os.mkdir(folder)
        print(f"Folder '{folder}' has been created!")

    else:
        print(f"Folder '{folder}' already exists!")

    # list all files to folder
    filenames = ["file1.txt", "file2.txt", "file3.txt"]
    for f in filenames:
        path = os.path.join(folder, f)
        with open(path, "w") as file:
            file.write(f"This is {f}")
        print(f"Created file: {f}")

    print(f"\nFiles in {folder}:")
    for f in os.listdir(folder):
        print(f"- {f}")

    # rename one of the files
    old = os.path.join(folder, "file1.txt")
    new = os.path.join(folder, "updated_file.txt")
    if os.path.exists(old):
        os.rename(old, new)
        print(f"Renamed file: {old} to {new}")

    # clean up by removing all files and the folder
    print("\nCleaning up...")
    for f in os.listdir(folder):
        os.remove(os.path.join(folder, f))
        print(f"Removed file: {f}")
    os.rmdir(folder)
    print(f"Folder '{folder}' has been removed!")

file_manager_demo()

