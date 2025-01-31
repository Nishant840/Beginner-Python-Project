import os

def main():
    while True:
        print("🛠️ File management app 🛠️")
        print("Enter 1: to create a file")
        print("Enter 2: to view all files")
        print("Enter 3: to delete a file")
        print("Enter 4: to read a file")
        print("Enter 5: to edit a file")
        print("Enter 6: to close the app")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            filename = input("Enter the name of file you want to create: ")
            create_file(filename)

        elif choice == '2':
            viewAll_files()

        elif choice == '3':
            filename = input("Enter the file name you want to delete: ")
            delete_file(filename)

        elif choice == '4':
            filename = input("Enter the name of file you want to read: ")
            read_file(filename)

        elif choice == '5':
            filename = input("Enter the name of file you want to edit: ")
            edit_file(filename)

        elif choice == '6':
            print("Closing the app... ")
            break

        else :
            print("🧐 Please enter a value between 1 to 6 \n")


def create_file(filename) :
    try:
        with open(f"{filename}.txt", 'x') as file:
            print(f"File Name {filename}: created successfully !")

    except FileExistsError:
        print("File already exists!")

    except Exception as e:
        print("An error occured")


def viewAll_files():
    files = os.listdir()
    if not files:
        print("No file found")
    else:
        print("these files are present in directory 👇")
        for file in files:
            print(file)


def delete_file(filename):
    try:
        os.remove(filename)
        print(f"{filename} has been deleted successfully!")

    except FileNotFoundError:
        print("File doesn't exist")

    except Exception as e:
        print("An error occured!")

def read_file(filename):
    try:
        with open(f"{filename}.txt", "r") as file:
            content = file.read()
            print(f"content of {filename} is \n {content}")

    except FileNotFoundError:
        print("File not found!")

    except Exception as e:
        print("An error occured!")


def edit_file(filename):
    try:
        with open(f"{filename}.txt","a") as file:
            data = input("Enter data to add= ")
            file.write(data + "\n")
            print(f"data added to {filename} sucessfully! ")

    except FileNotFoundError:
        print("File not found")
    
    except Exception as e:
        print("An error occured!")

if __name__ == "__main__":
    main()
