def solution(genres, plays):
    answer = []

    total = {}
    songs = {}

    for i in range(len(genres)):
        genre = genres[i]

        if genre not in total:
            total[genre] = plays[i]
            songs[genre] = []
        else:
            total[genre] += plays[i]

        songs[genre].append([-plays[i], i])

    genre_list = []

    for genre in total:
        genre_list.append([total[genre], genre])

    genre_list.sort(reverse=True)

    for data in genre_list:
        genre = data[1]

        songs[genre].sort()

        for song in songs[genre][:2]:
            answer.append(song[1])

    return answer