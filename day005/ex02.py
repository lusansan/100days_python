student_scores = input("Input a list of student scores.\n").split()
for n in range(0,len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

high_score = 0
for i in student_scores:
    if i > high_score:
        high_score = i

print(f"The highest score in the class is {high_score}")