# https://jungol.co.kr/problem/5805

import sys

def calculate_tosses(X, Y):
    Z = Y * 100 // X
    if Z == 100:
        return -1
    
    low = X + 1
    high = sys.maxsize
    while low <= high:
        new_X = low // 2 + high // 2
        res = new_X - X
        new_Y = Y + res
        new_Z = new_Y * 100 // new_X
        # print(new_X, new_Y, new_Z)
        if new_Z > Z:
            if (new_Y - 1) * 100 // (new_X - 1) == Z:
                return res
            else:
                high = new_X
        else:
            if new_X + 1 == low:
                break
            low = new_X + 1
    return -1

X, Y = map(int, input().split())
print(calculate_tosses(X, Y))