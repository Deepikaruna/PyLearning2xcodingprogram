# we will ask user which browser want to use for automation

browser = input("Enter the browser name\n")
match browser:
    case "chrome":
        print("Chrome code executed!")
    case "firefox":
        print("firefox code executed!")
    case _:
        print("No browser found!")