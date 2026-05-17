def solution(phone_book):
    dic = {}

    for number in phone_book:
        dic[number] = 1

    for number in phone_book:
        temp = ""

        for num in number:
            temp += num

            if temp in dic and temp != number:
                return False

    return True