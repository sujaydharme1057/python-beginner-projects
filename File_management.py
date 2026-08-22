import os

def create_file(filename):
    try:
        with open(filename, "x") as f:
            print(f"File Name {filename}: Created Succesfully!")
    except FileExistsError:
        print(f"File Name {filename} already exists")
    except Exception as e:
        print("An Error Occurred!")

def view_all_files():
    files = os.listdir()
    if not files:
        print("No Files found!")
    else:
        print("Files in Directory!")
        for file in files:
            print(file)

def delete_file(filename):
    try:
        os.remove(filename)
        print(f"{filename} has been deleted succesfully!")
    except FileNotFoundError:
        print("File Not Found!")
    except Exception as e:
        print("An error Occured")

def read_file(filename):
    try:
        with open(filename, "r") as f:
            content = f.read()
            print(f"Content of {filename} :\n{content}")
    except FileNotFoundError:
        print("file Name does not found")
    except Exception as e:
        print("An error Occrued")

def edit_file(filename):
    try:
        with open(filename, "a") as f:
            content = input("Enter the data you want to add : ")
            f.write(content + "\n")
        print(f"Content added to {filename} Succesfully!")
    except FileNotFoundError:
        print(f"{filename} doesn't exist")
    except Exception as e:
        print("An error Occurred")

def main():
    while True:
        print("File Managment App")
        print("1: Create file")
        print("2: View all file")
        print("3: Delete file")
        print("4: Read file")
        print("5: Edit file")
        print("6: Exit")

        choice = input("Enter your choice = ")

        if choice == "1":
            filename = input("Enter the filename to create : ")
            create_file(filename)
        elif choice == "2":
            view_all_files()
        elif choice == "3":
            filename = input("Enter the file Name you Want to Delete : ")
            delete_file(filename)
        elif choice == "4":
            filename = input("Enter the file you want to read : ")
            read_file(filename)
        elif choice == "5":
            filename = input("Enter the File name you want to Edit: ")
            edit_file(filename)
        elif choice == "6":
            print("Closing the app....")
            break
        else:
            print("Invalid Syntax")

if __name__ == "__main__":
    main()