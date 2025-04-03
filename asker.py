def get_int(prompt):
    while True:
        x = input(prompt)
        #Check if x is a number and print error message
        if x.isnumeric() == False:
            print("Input must be an int")
        else:
            return int(x)

if __name__ == "__main__":
    name = input("What is your name: ")
    age = get_int("What is your age: ")
    lucky_number = get_int("What is your lucky number: ")

    print(f"Hello {name} you are {age} years old and your lucky number is {lucky_number}")
