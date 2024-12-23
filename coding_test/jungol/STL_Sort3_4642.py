# https://jungol.co.kr/problem/4642?cursor=eyJwcm9ibGVtc2V0Ijo4LCJmaWVsZCI6MCwiaWR4Ijo1fQ==

class student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __lt__(self, other):
        if self.score != other.score:
            return self.score > other.score
        else:
            return self.name < other.name

students = []
n = int(input())
for _ in range(n):
    name, score = input().split()
    score = int(score)
    st = student(name, score)
    students.append(st)

students.sort()
for st in students:
    print(st.name, st.score)