# 19532
# 수학은 비대면강의입니다

# def solution():
#     a,b,c,d,e,f = map(int, input().split())
#     for x in range(-999, 1000):
#         for y in range(-999, 1000):
#             if a * x + b * y == c and d * x + e * y == f:
#                 return x, y
            
# result = solution()
# print(*result)

a,b,c,d,e,f = map(int, input().split())
x = (c*e - b*f) // (a*e - b*d)
y = (a*f - c*d) // (a*e - b*d)

print(x, y)