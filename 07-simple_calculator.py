user_input = input("What equation do you want to do?(addition(a), subtraction(s), multiplication(m), division(d)")
number1 = int(input("What is your first number?"))
number2 = int(input("What is your second number?"))

if user_input == "addition":
    answer = number1 + number2
    print(f"{number1} + {number2} = {answer}")
elif user_input == "subtraction":
    answer = number1 - number2
    print(f"{number1} - {number2} = {answer}")
elif user_input == "multiplication":
    answer = number1 * number2
    print(f"{number1} x {number2} = {answer}")
elif user_input == "division":
    answer = number1 // number2
    print(f"{number1} / {number2} = {answer}")
else:
    print("Please enter the option correctly")





