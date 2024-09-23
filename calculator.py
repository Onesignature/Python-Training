operator = input("Enter an operator( + - * / ) ")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))


if operator == '+':
    answer = num1 + num2
    print(f"{num1} {operator} {num2} = {answer}")
elif operator == '-':
    answer = num1 - num2
    print(f"{num1} {operator} {num2} = {answer}")
elif operator == '*':
    answer = num1 * num2
    print(f"{num1} {operator} {num2} = {answer}")
elif operator == '/':
    answer = num1 / num2
    print(f"{num1} {operator} {num2} = {answer}")

else:
    print("Operator not valid, run program again.")