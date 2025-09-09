# simple calculator
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

print("sum:", a+b)
print("subtraction:", a-b)
print("multiplication:", a*b)

if b != 0:   # check b is NOT zero
    print("quotient:", a/b)
else:
    print("cannot divide by zero")