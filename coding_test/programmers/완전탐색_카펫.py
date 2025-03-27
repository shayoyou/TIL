def solution(brown, yellow):
    for h in range(1, yellow + 1):
        if yellow % h == 0:
            w = yellow // h
            if (w + 2) * (h + 2) == brown + yellow:
                return [w + 2, h + 2]


print(solution(10, 2))