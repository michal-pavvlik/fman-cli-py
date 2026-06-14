import os

print("""    ____________    __  ______    _   __
   / ____/  _/ /   /  |/  /   |  / | / /
  / /_   / // /   / /|_/ / /| | /  |/ / 
 / __/ _/ // /___/ /  / / ___ |/ /|  /  
/_/   /___/_____/_/  /_/_/  |_/_/ |_/  """)

operations_possibilities = range(1,6)

def addNewFile():
    new_file_name = input("Name of the file to create (with format): ")
    if(os.path.isfile(new_file_name)):
        print("File alerady exists!")
        return
    with open(new_file_name, 'w') as nf:
        pass

def main():
    while(True):
        print("What operation would you like to do:\n1. Add file\n2. Delete file\n3. Edit file\n4. Change directory\n5. Exit")
        operation_id = input()
        while(int(operation_id) not in operations_possibilities):
            print("Wrong input, write down a value from 1 to 5")
            operation_id = input()
        match int(operation_id):
            case 1:
                addNewFile()
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                print("Shutting down the program.")
                return
if __name__ == "__main__":
    main()