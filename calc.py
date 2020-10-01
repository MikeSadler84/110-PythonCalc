# functions
def print_menu():
    print("-" * 20)
    print("Python Calculator")
    print("-" * 20)

    print("[1] Add")
    print("[2] Subtract")
    print("[3] Divide")
    print("[4] Multiply")

    print("[5] My Age")

    print("[x] Close")


"""
option 5
ask for birth year
I will tell you the age (+/-)

"""


# instructions

# Used the while loop to make the program restart automatically
option = ""
current_year = "2020"
while(option != "x"):
    print_menu()
    # use input when you want the user to be able to type information
    option = input("Please choose an option: ")
    if(option != "x" and option != "5"):
        num1 = input("First number: ")
        num2 = input("Second number: ")
    if(option == "1"):
        res = float(num1) + float(num2)
        print("Result: " + str(res))
    elif(option == "2"):
        res = float(num1) - float(num2)
        print("Result: " + str(res))
    elif(option == "3"):
        if(num2 == "0"):
            print("-" * 20)
            print("Cannot divide by 0!")
            print("-" * 20)
        else:
            res = float(num1) / float(num2)
            print("Result: " + str(res))
    elif(option == "4"):
        res = float(num1) * float(num2)
        print("Result: " + str(res))
    elif(option == "5"):
        year = input("What year were you born: ")
        res = int(current_year) - int(year)
        print("You are " + str(res) + " years old.")


print("-" * 20)
print("Program closed!")
print("-" * 20)
