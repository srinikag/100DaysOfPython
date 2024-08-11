sum_of_even = 0
sum_of_odd = 0
for num in range(0, 101):
    number = num % 2
    if number == 0:
        sum_of_even += num
    else:
        sum_of_odd = sum_of_odd + num


print(f"Sum of all even numbers are {sum_of_even}")
print(f"Sum of all odd numbers are {sum_of_odd}")