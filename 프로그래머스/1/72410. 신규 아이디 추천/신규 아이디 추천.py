def solution(new_id):
    new_id = new_id.lower()

    temp = ""
    for c in new_id:
        if ('a' <= c <= 'z') or ('0' <= c <= '9') or c in "-_.":
            temp += c
    new_id = temp

    temp = ""
    for c in new_id:
        if not (temp and temp[-1] == "." and c == "."):
            temp += c
    new_id = temp

    new_id = new_id.strip(".")

    if new_id == "":
        new_id = "a"

    new_id = new_id[:15]
    new_id = new_id.rstrip(".")

    while len(new_id) < 3:
        new_id += new_id[-1]

    return new_id