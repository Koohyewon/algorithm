def solution(gems):
    total = len(set(gems))

    count = {}          # 현재 구간에 들어 있는 보석별 개수
    now = 0             # 현재 구간에 들어 있는 보석 종류 수

    answer = [1, len(gems)]
    best = len(gems)    # 구간 길이 기준

    left = 0
    for right in range(len(gems)):
        gem = gems[right]

        if gem in count:
            count[gem] = count[gem] + 1
        else:
            count[gem] = 1
            now = now + 1

        # 모든 종류를 포함하면 왼쪽을 줄여본다
        if now == total:
            while left <= right:
                out = gems[left]
                if count[out] == 1:
                    break
                count[out] = count[out] - 1
                left = left + 1

            length = right - left + 1     
            if length < best:
                best = length
                answer = [left + 1, right + 1]

    return answer