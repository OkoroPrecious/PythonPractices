# A class of ten students took a quiz. Their grades (integers in the range 0 – 100) are
# 98, 76, 71, 87, 83, 90, 57, 79, 82, 94. Determine the class average on the quiz.

total = 0
grade_counter = 0

grades = [98, 76, 71, 87, 83, 90, 57, 79, 82, 94]

for grade in grades:
    total += grade
    grade_counter += 1

average = total / grade_counter
print(f'Class average is {average}')
