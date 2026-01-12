def calculator():
    print("whats your choice")
    print("1 is addition")
    print("2 is subtraction")
    print("3 is multiplication")
    print("4 is division")

    choice = input("what do you choose from the option: ")

    num_1 = int(input("whats your first number: "))
    num_2 = int(input("whats your second number: "))

    if choice == "1":
        print("Addition is", num_1 + num_2)

    elif choice == "2":
        print("Subtraction is", num_1 - num_2)

    elif choice == "3":
        print("Multiplication is", num_1 * num_2)

    elif choice == "4":
        print("Division is", num_1 / num_2)

    else:
        print("Invalid choice")

calculator()





