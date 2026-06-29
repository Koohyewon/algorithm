def solution(word):
    alpha = ["A", "E", "I", "O", "U"]

    answer = 0
    count = 0

    def dfs(s):
        nonlocal answer, count

        if s:
            count += 1

            if s == word:
                answer = count
                return

        if len(s) == 5:
            return

        for ch in alpha:
            dfs(s + ch)

    dfs("")

    return answer