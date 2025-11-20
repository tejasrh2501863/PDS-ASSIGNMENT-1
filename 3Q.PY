# Program to calculate total, average and grade of a student

# Taking inputs
name = input("Enter the student's name: ")

# Input marks with validation
marks = []
for i in range(1, 4):
    mark = float(input(f"Enter marks for subject {i}: "))
    if mark < 0 or mark > 100:
        print("Error: Marks must be between 0 and 100.")
        exit()   # Stop program if invalid marks
    marks.append(mark)

# Calculations
total = sum(marks)
average = total / 3

# Grade calculation
if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

# Output section
print("\n----- STUDENT REPORT -----")
print("Name:", name)
print("Total Marks:", total)
print("Average Marks:", round(average, 2))
print("Grade:", grade)
