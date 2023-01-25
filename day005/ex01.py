student_heights = input("Input a list of student heights.\n").split()
for n in range (0,len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

height_sum = 0
student_count = 0
for i in (student_heights):
    height_sum += i 
    student_count += 1

print(height_sum/student_count)