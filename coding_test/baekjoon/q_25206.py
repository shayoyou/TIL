# 25206
# 너의 평점은

grades = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}
sum = 0.0
grade_sum = 0.0
for _ in range(20):
    course, score, grade = input().split()
    score = float(score)
    if grade == 'P':
        continue
    sum += score * grades[grade]
    grade_sum += score
print(f'{sum / grade_sum:.6f}')