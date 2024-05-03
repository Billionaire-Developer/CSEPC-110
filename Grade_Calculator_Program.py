#Ask for grade percentage
grade_percentage = float(input("Enter your grade percentage (0-100): "))

#Determine the letter grade
if grade_percentage >= 90:
    letter = "A"
elif grade_percentage >= 80:
    letter = "B"
elif grade_percentage >= 70:
    letter = "C"
elif grade_percentage >= 60:
    letter = "D"
else:
    letter = "F"

#print the letter grade
print("Your grade is:", letter)

#Determine if the user passed the course
if grade_percentage >= 70:
    print("congratulations, you passed the course!")
else:
    print("don't worry, you'll do better next time!")