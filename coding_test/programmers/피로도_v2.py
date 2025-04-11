from itertools import permutations

def solution(k, dungeons):
    answer = 0
    for item in permutations(dungeons):
        fatigue = k
        count = 0
        for need, use in item:
            if fatigue >= need:
                count += 1
                fatigue -= use
        answer = max(answer, count)
    return answer

print(solution(80, [[80,20],[50,40],[30,10]]))