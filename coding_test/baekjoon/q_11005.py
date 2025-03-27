# 11005
# 진법 변환 2

n, b = map(int, input().split())
result = ''

while n > 0:
    remain = n % b
    result += str(remain) if remain < 10 else chr(remain + 55)
    n //= b

print(result[::-1])
