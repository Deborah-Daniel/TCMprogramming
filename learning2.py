"""
learning how to build a basic calculator
"""

#example from course: practice basic

a = float(input("Provide a number: "))
b = input("give me an operator: ")
c  = float(input("provide another number: "))


if b == "+":
    print(a + c)
elif b == "-":
    print(a - c)
elif b == "/":
    print(a / c)
elif b == "**" or b == "^":
    print(a ** c)
else:
    print("Unknown operator.")