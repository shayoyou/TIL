def get_solve_time(level, diff, time, prev_time):
    if diff <= level:
        return time
    else:
        return (time + prev_time) * (diff - level) + time
        
def solution(diffs, times, limit):
    answer = 0
    low = min(diffs)
    high = max(diffs)

    while low <= high:
        level = (low + high) // 2
        total = 0
        prev_time = 0
        for i in range(len(diffs)):
            if i > 0:
                prev_time = times[i - 1]
            total += get_solve_time(level, diffs[i], times[i], prev_time)
            if total > limit:
                total = -1
                break

        # print(level, total)

        if total == -1:
            low = level + 1
        else:
            answer = level
            high = level - 1
    
    return answer


if __name__ == '__main__':
    # res = solution([1,5,3], [2,4,7], 30)
    # res = solution([1,4,4,2], [6,3,8,2], 59)
    # res = solution([1, 328, 467, 209, 54], [2, 7, 1, 4, 3], 1723)
    res = solution([1, 99999, 100000, 99995], [9999, 9001, 9999, 9001], 3456789012)
    print(res)