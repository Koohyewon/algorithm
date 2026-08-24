def solution(n, info):
    answer = [-1]
    max_diff = 0

    def dfs(idx, arrows, ryan):
        nonlocal answer, max_diff

        # 11개 점수를 모두 확인
        if idx == 11:
            # 남은 화살은 0점에 사용
            ryan[10] += n - arrows

            ryan_score = 0
            apeach_score = 0

            for i in range(11):
                score = 10 - i

                if ryan[i] > info[i]:
                    ryan_score += score
                elif info[i] > 0:
                    apeach_score += score

            diff = ryan_score - apeach_score

            if diff > 0:
                # 점수 차이가 더 큰 경우
                if diff > max_diff:
                    max_diff = diff
                    answer = ryan[:]

                # 점수 차이가 같은 경우
                elif diff == max_diff:
                    # 낮은 점수부터 비교
                    for i in range(10, -1, -1):
                        if ryan[i] > answer[i]:
                            answer = ryan[:]
                            break
                        elif ryan[i] < answer[i]:
                            break

            ryan[10] -= n - arrows
            return

        # 현재 점수에서 필요한 화살 수
        need = info[idx] + 1

        # 1. 현재 점수를 가져가는 경우
        if arrows + need <= n:
            ryan[idx] = need
            dfs(idx + 1, arrows + need, ryan)
            ryan[idx] = 0

        # 2. 현재 점수를 포기하는 경우
        dfs(idx + 1, arrows, ryan)

    dfs(0, 0, [0] * 11)

    return answer