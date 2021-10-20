def message(option):
    if option == 1:
        print("Option 1")
    elif option == 2:
        print("Option 2")
    elif option == 3:
        print("Option 3")
    else:
        print("Unknown")
    return "I'm back"


print(message(int(input("choose an option: "))))
