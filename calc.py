operator = input("Enter operator (+, -, * or /): ");
num1 = float(input("Enter the first number: "));
num2 = float(input("Enter the second number: "));

if operator == "+":
    answer = num1 + num2;
    print(round(answer, 5));
elif operator == "-":
    answer = num1 - num2;
    print(round(answer, 5));
else:
    print(f"{operator} is not valid.");