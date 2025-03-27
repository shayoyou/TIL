def solution(sizes):
    # w, h = 0, 0
    # for i, size in enumerate(sizes):
    #     if size[0] < size[1]:
    #         size[0], size[1] = size[1], size[0]
    #     if w < size[0]:
    #         w = size[0]
    #     if h < size[1]:
    #         h = size[1]
    # return w * h
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)


print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))