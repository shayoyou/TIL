# 2869
# 달팽이는 올라가고 싶다

a, b, v = map(int, input().split())
day = (v - b) / (a - b)
if day == int(day):
    day = int(day)
else:
    day = int(day) + 1
print(day)