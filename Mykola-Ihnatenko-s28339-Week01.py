# Task 1
#print(input("Enter first name: ") + " " + input("Enter last name: ") + " " + input("Enter age: "))

# Task 2
fahrenheit = float(input("Enter temperature in fahrenheit: "))
celsius = (fahrenheit - 32) * 5 / 9
print("Temperature in celsius:", celsius)

# Task 3
score = float(input("Enter your score: "))

if score >= 90:
    grade = 5
elif score >= 80:
    grade = 4
elif score >= 70:
    grade = 3
elif score >= 60:
    grade = 2
else:
    grade = 1

print("Your grade is:", grade, "; work in class: " + str(round(score * 0.2, 2)), "; test: " + str(round(score * 0.3, 2)), "; project: " +
      str(score * 0.5) + ".")

# Task 4
number = int(input("Enter a number: "))
number2 = int(input("Enter a number: "))

if number % number2 == 0:
    result = "True " + str(number/number2)
else:
    result = "False " + str(number/number2)

# Print the result
print(result)

# Task 5
# Define variables
side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

# Check the type of triangle
if side1 > side2 + side3 or side2 > side3 + side1 or side3 > side2 + side1:
    triangle_type = "not exist"
elif side1 == side2 == side3:
    triangle_type = "Equilateral"
elif side1 == side2 or side1 == side3 or side2 == side3:
    triangle_type = "Isosceles"
else:
    triangle_type = "Scalene"

# Print the type of triangle
print("The triangle is:", triangle_type)

# Task 6
# Define variables
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

# Perform the operation
if num2 == 0:
    print("Numbers can't be divided by 0")
elif operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2
else:
    result = "Invalid operation"

# Print the result
if num2 != 0:
    print("Result:", result)