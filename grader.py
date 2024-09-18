possible_grades = ["A", "B", "C", "D", "F"]
total_points = int(input("Enter the total amount of possible points: "))
points = int(input("Enter the amount of points the student got: "))
score = (points/total_points)*100

if score <= 50:
    print("The students grade is a(n):", possible_grades[-1])
elif score > 50 and score <= 60:
    print("The students grade is a(n):", possible_grades[3])
elif score > 60 and score <= 75:
    print("The students grade is a(n):", possible_grades[2])
elif score > 75 and score <= 88:
    print("The students grade is a(n):", possible_grades[1])
else:
    print("The students grade is a(n):", possible_grades[0])
