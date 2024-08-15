cond = True
while cond:
    user_input = input("What equation do you want to do?(addition-a, subtraction-s, multiplication-m, division-d, or "
                       "exit-q)")
    if user_input == "q":
        print("Goodbye!")
        cond = not cond
    else:
        number1 = int(input("What is your first number?"))
        number2 = int(input("What is your second number?"))
        if user_input == "a":
            answer = number1 + number2
            print(f"{number1} + {number2} = {answer}")
        elif user_input == "s":
            answer = number1 - number2
            print(f"{number1} - {number2} = {answer}")
        elif user_input == "m":
            answer = number1 * number2
            print(f"{number1} x {number2} = {answer}")
        elif user_input == "d":
            answer = number1 / number2
            print(f"{number1} / {number2} = {answer}")
        else:
            print("Please enter the option correctly")





