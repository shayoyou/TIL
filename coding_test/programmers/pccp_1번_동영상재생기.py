# https://school.programmers.co.kr/learn/courses/30/lessons/340213

def time_to_seconds(time_str):
    dev = list(map(int, time_str.split(":")))
    return dev[0] * 60 + dev[1]

def seconds_to_time(t):
    return f"{t // 60:02d}:{t % 60:02d}"

def solution(video_len, pos, op_start, op_end, commands):
    _vedio_len = time_to_seconds(video_len)
    _pos = time_to_seconds(pos)
    _op_start = time_to_seconds(op_start)
    _op_end = time_to_seconds(op_end)
    
    if _pos >= _op_start and _pos <= _op_end:
        _pos = _op_end

    for cmd in commands:
        if cmd == "prev":
            _pos = max(0, _pos - 10)
        else: # next
            _pos = min(_vedio_len, _pos + 10)

        if _pos >= _op_start and _pos <= _op_end:
            _pos = _op_end

    return seconds_to_time(_pos)


if __name__ == "__main__":
    print(solution("34:33",	"13:00", "00:55", "02:55", ["next", "prev"]))
    print(solution("10:55",	"00:05", "00:15", "06:55", ["prev", "next", "next"]))
    print(solution("07:22", "04:05", "00:15", "04:07", ["next"]))
    
    
