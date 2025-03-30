def solution(wallet, bill):
    answer = 0
    w = bill[0]
    h = bill[1]
    while True:
        if wallet[0] >= w and wallet[1] >= h or wallet[0] >= h and wallet[1] >= w:
            break
        if w > h:
            w //= 2
        else:
            h //= 2
        answer += 1
    return answer


print(solution([30,15], [26,17]))
print(solution([50,50], [100,241]))