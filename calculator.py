"""Simple console calculator supporting +, -, *, / operations."""

a = int(input())
op = input()
b = int(input())
if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    if b == 0:
        print("Cannot divide by zero")
    else: 
        print(a / b)  
else:
    print("Invalid operation")
