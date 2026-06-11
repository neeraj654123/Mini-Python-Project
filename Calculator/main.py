try:
    a = int(input("Enter 1st no.: " ))
    b = int(input("Enter 2nd no.: "))

    print(f"What kind of operation do you want toperform.\nPress + for addition \n- for subraction \n* for multiplication \n/ for division")

    O =input("Enter operation: ")

    match O:
        case "+":
            print(f"The result is : {a+b}")
        case "-":
            print(f"The result is : {a-b}")
        case "*":
            print(f"The result is : {a*b}")
        case "/":
            print(f"The result is : {a/b}")
        case default:
            print("There was an error")

except Exception as e:
    print("Enter a valid value of a and b")