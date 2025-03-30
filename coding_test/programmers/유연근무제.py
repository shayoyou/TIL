def solution(schedules, timelogs, startday):
    day = startday
    check = [1] * len(schedules)
    for i in range(len(timelogs[0])):
        if day < 6:
            for j in range(len(check)):
                if check[j] == 1:
                    limit_time = schedules[j] + 10
                    if limit_time % 100 >= 60:
                        limit_time += 40
                    if timelogs[j][i] > limit_time:
                        check[j] = 0
        
        day = day % 7 + 1
    return check.count(1)


print(solution([700, 800, 1100], [[710, 2359, 1050, 700, 650, 631, 659], [800, 801, 805, 800, 759, 810, 809], [1105, 1001, 1002, 600, 1059, 1001, 1100]], 5))
print(solution([730, 855, 700, 720], [[710, 700, 650, 735, 700, 931, 912], [908, 901, 805, 815, 800, 831, 835], [705, 701, 702, 705, 710, 710, 711], [707, 731, 859, 913, 934, 931, 905]], 1))