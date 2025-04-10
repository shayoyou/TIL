from queue import PriorityQueue

def solution(scoville, K):
    answer = 0
    priority_queue = PriorityQueue()
    for s in scoville:
        priority_queue.put(s)
    
    while True:
        first = priority_queue.get()
        if first >= K:
            break
        if priority_queue.empty():
            answer = -1
            break
        second = priority_queue.get()
        priority_queue.put(first + second * 2)
        answer += 1

    return answer

print(solution([1, 2, 3, 9, 10, 12], 7))