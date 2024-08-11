# Question: Ask the user what the dividend and divisor is and give the quotient
# Ask the user what the dividend and divisor is
dividend = int(input("What is you dividend?"))
divisor = int(input("What is you divisor?"))
# Divide dividend and divisor, get the quotient and remainder
quotient = dividend//divisor
remainder = dividend % divisor
# Print quotient and remainder
print(f"Your quotient is {quotient} and {remainder} remainder")
