def solution(user_id, banned_id):
    result = []

    def is_match(user, ban):
        if len(user) != len(ban):
            return False

        for i in range(len(ban)):
            if ban[i] == "*":
                continue
            if ban[i] != user[i]:
                return False

        return True

    def dfs(idx, picked):
        if idx == len(banned_id):
            tmp = []
            for p in picked:
                tmp.append(p)
            tmp.sort()

            if tmp not in result:
                result.append(tmp)
            return

        for user in user_id:
            if user in picked:
                continue
            if is_match(user, banned_id[idx]):
                picked.append(user)
                dfs(idx + 1, picked)
                picked.pop()

    dfs(0, [])

    return len(result)