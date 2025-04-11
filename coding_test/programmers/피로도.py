from collections import deque

def solution(k, dungeons):
    
    def func(fatigue, depth, dq: deque):
        cnt = len(dq)
        if cnt == 0:
            return depth

        res = depth
        for i in range(cnt):
            dungeon = dq.popleft()
            if fatigue >= dungeon[0]:
                res = max(res, func(fatigue - dungeon[1], depth + 1, dq))
            dq.append(dungeon)

        return res
        
    dungeons_deque = deque(dungeons)
    return func(k, 0, dungeons_deque)

print(solution(80, [[80,20],[50,40],[30,10]]))