# 10988
# 팰린드롬인지 확인하기

word = input()
reverse = word[::-1]
if word == reverse:
    print(1)
else:
    print(0)