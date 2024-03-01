# Task 1
#print(input("Enter first name: ") + " " + input("Enter last name: ") + " " + input("Enter age: "))

# Task 2
"""fahrenheit = float(input("Enter temperature in fahrenheit: "))
celsius = (fahrenheit - 32) * 5 / 9
print("Temperature in celsius:", celsius)"""

# Task 3
score = float(input("Enter your score: "))

# Determine the grade
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