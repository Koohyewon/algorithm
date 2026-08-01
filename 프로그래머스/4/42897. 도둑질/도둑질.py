def solution(money):

    def rob(nums):
        two_before = 0  
        one_before = 0  

        for num in nums:
            current = max(one_before, two_before + num)

            two_before = one_before
            one_before = current

        return one_before

    case1 = rob(money[:-1])
    case2 = rob(money[1:])

    return max(case1, case2)