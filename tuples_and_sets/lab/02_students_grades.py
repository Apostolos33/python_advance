number_of_students = int(input())

students_and_their_grades = {}

for _ in range(number_of_students):
    student, grade = input().split()
    if student not in students_and_their_grades:
        students_and_their_grades[student] = []
    students_and_their_grades[student].append(float(grade))

for student, grades in students_and_their_grades.items():
    avg = sum(grades) / len(grades)
    formatted_grades = ' '.join([f'{el:.2f}' for el in grades])
    print(f"{student} -> {formatted_grades} (avg: {avg:.2f})")