operator = input("Enter an operator(+-*/):")
Num1 = float(input("Enter number 1 = "))
Num2 = float(input("Enter number 2 = "))
if operator == '+':
    result = Num1 + Num2
    print(round(result, 4))
   
elif operator == '-':
    result = Num1 - Num2
    print(round(result, 4))
elif operator == '*':
    result = Num1 * Num2
    print(round(result, 4))
elif operator == '/':
    result = Num1 / Num2
    print(round(result, 4))
else:
    print("wrong choice hahahahha")
