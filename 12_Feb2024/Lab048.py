# Match - It is similar to switch case

numbers = int(input("Enter a number\n"))

match numbers:
    case 1:
        print("You have entered 1")
    case 2:
        print("You have entered 2")
    case 3:
        print("You have entered 3")
    case 4:
        print("You have entered 4")
    case _:
        print("No idea")
