# Welcome message
print(" We will perform basic mathematical operations on two numbers,")

# Input from user
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

# Display Results
print("The results are as follows:")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)

#If user enters b as 0
if b>0 or b<0:
    print("Division:", a / b)
else :
    print("Division:Not defined")