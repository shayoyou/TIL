# 2745
# 진법 변환

n, b = input().split()
b = int(b)
result = 0
for i, digit in enumerate(reversed(n)):
    if '0' <= digit <= '9':
        result += int(digit) * (b ** i)
    else:
        result += (ord(digit) - ord('A') + 10) * (b ** i)

print(result)