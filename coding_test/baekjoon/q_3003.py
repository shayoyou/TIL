# 킹, 퀸, 룩, 비숍, 나이트, 폰

counts = [1,1,2,2,2,8]
answer = [counts[i] - count for i, count in enumerate(map(int, input().split()))]
print(*answer)