def addition(num1, num2):
    answer = number1 + number2
    print(f"{number1} + {number2} = {answer}")


def subtraction(num1, num2):
    answer = number1 - number2
    print(f"{number1} - {number2} = {answer}")


def multiplication(num1, num2):
    answer = number1 * number2
    print(f"{number1} x {number2} = {answer}")


def division(num1, num2):
    answer = number1 / number2
    print(f"{number1} / {number2} = {answer}")



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
            addition(number1, number2)
        elif user_input == "s":
            subtraction(number1, number2)
        elif user_input == "m":
            multiplication(number1, number2)
        elif user_input == "d":
            division(number1, number2)
        else:
            print("Please enter the option correctly")





