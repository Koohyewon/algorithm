def solution(babbling):
    sounds = ["aya", "ye", "woo", "ma"]
    answer = 0

    for word in babbling:
        prev = ""

        while word:
            found = False

            for sound in sounds:
                # 이전 발음과 같으면 연속해서 발음한 것이므로 불가능
                if sound == prev:
                    continue

                # 현재 단어의 앞부분이 발음 가능한 발음인지 확인
                if word.startswith(sound):
                    word = word[len(sound):]
                    prev = sound
                    found = True
                    break

            # 어떤 발음으로도 시작할 수 없다면 불가능한 단어
            if not found:
                break

        # 모든 문자열을 발음으로 만들었다면 정답
        if not word:
            answer += 1

    return answer