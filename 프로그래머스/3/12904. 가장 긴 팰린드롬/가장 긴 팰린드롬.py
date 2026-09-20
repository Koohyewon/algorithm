def solution(s):
    n = len(s)
    answer = 1

    def expand(left, right):
        length = 0

        while left >= 0 and right < n:
            if s[left] != s[right]:
                break
            length = right - left + 1
            left = left - 1
            right = right + 1

        return length

    for i in range(n):
        odd = expand(i, i)        
        even = expand(i, i + 1)   

        if odd > answer:
            answer = odd
        if even > answer:
            answer = even

    return answer