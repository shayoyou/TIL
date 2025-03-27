def solution(num):
    answer = []
    def hanoi(num, start, target, temp):
        if num == 1:
            answer.append([start, target])
            return
        
        hanoi(num - 1, start, temp, target)
        answer.append([start, target])
        hanoi(num - 1, temp, target, start)

    hanoi(num, 1, 3, 2)
    return answer

print(solution(3))