import sys

def solve():
    # 입력을 받아서 정수로 변환해 (입력이 비어있을 경우를 대비해 예외처리 살짝!)
    input_data = sys.stdin.read().strip()
    if not input_data:
        return
    
    n = int(input_data)

    # 1인 경우 아무것도 출력하지 않아
    if n == 1:
        return

    # 2부터 시작해서 나누어 떨어지는지 확인해
    # i * i <= n 은 i <= sqrt(n)과 같아서 연산량을 획기적으로 줄여줘!
    i = 2
    while i * i <= n:
        while n % i == 0:
            print(i)
            n //= i
        i += 1
    
    # 마지막에 남은 n이 1보다 크다면, 그 자체가 마지막 소인수야
    if n > 1:
        print(n)

if __name__ == "__main__":
    solve()
