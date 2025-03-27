from itertools import permutations

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    for i in range(5, int(num**0.5) + 1, 6):
        if num % i == 0 or num % (i + 2) == 0:
            return False
    return True

def solution(numbers):
    nums = [n for n in numbers]
    permu = []
    for i in range(1, len(numbers) + 1):
        permu += list(permutations(nums, i))
    
    new_nums = set()
    for p in permu:
        new_nums.add(int("".join(p)))
    
    count = 0
    for num in new_nums:
        if is_prime(num):
            count += 1
            
    return count

print(solution("011"))