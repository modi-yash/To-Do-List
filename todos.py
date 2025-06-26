import sys
# Makes to_do_list file if it doesn't exist
# Defaults to 1. Walk the Dog, 2. Buy cheese
def add_to_do(to_do:str):
    with open("to_do_list.txt", "a") as file:
            file.write('\n'+sys.argv[2])
def remove_to_do(num:int):
    if(num<=0):
        raise ValueError("The integer value must be greater than zero!")
    with open("to_do_list.txt", "r") as file:
        lines = file.readlines()
        del lines[num]
    with open("to_do_list.txt", "w") as file:
        
def print_to_do():
    num_line = 0
    with open("to_do_list.txt","r") as file:
        lines = file.readlines()
        print("Here's your ToDo list:\n")
        for line in lines:
            print(f"{num_line}. {line}", end="")
            num_line+=1

try:
    with open("to_do_list.txt", "x") as file:
        file.write("1. Walk the Dog\n2. Buy cheese")
except FileExistsError as e:
    pass
except Exception as e:
    print("An unknown error occurred:", e)
    sys.exit(1)

if len(sys.argv)==1:
    try:
        print_to_do()
    except Exception as e:
        print("An unknown error occurred:", e)
        sys.exit(1)
elif sys.argv[1]=="add":
    try:
        add_to_do(sys.argv[2])
    except Exception as e:
        print("An unknown error occurred:", e)
        sys.exit(1)
elif sys.argv[1]=="remove":
    try:
        remove_to_do(int(sys.argv[2]))
    except ValueError as e:
        print("ValueError: You need to put an integer value!", e)
        sys.exit(1)
    except Exception as e:
        print("An unknown error occurred:", e)
        sys.exit(1)


# Remove Todo

# Save File

# Print List

# print("\nHere's your ToDo list:\n")
# print("1. Walk the Dog")
# print("2. Buy cheese")

# Print Commands
print("\n\n*********************************\n")
print(f"To view ToDos:\n{sys.argv[0]}")
print(f"\nTo add a ToDo:\n{sys.argv[0]} add \"Clean Room\"\n")
print(f"To remove or complete ToDo:\n{sys.argv[0]} remove 2\n")
