def solution(s):
    # 앞의 "{{"와 뒤의 "}}"를 떼고 "},{" 기준으로 집합을 나눈다
    groups = []
    for part in s[2:-2].split("},{"):
        numbers = []
        for x in part.split(","):
            numbers.append(int(x))
        groups.append([len(numbers), numbers])

    # 원소 개수가 적은 집합부터 오도록 정렬
    groups.sort()

    answer = []
    seen = set()  # 이미 답에 넣은 숫자
    for size, numbers in groups:
        for number in numbers:
            # 앞 집합에 없던 새 숫자만 답에 넣는다
            if number not in seen:
                seen.add(number)
                answer.append(number)

    return answer