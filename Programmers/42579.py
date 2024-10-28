# 가장 많이 재생된 장르 수록
# 장르 내에서 가장 많이 재생된 노래 수록
# 장르 내 재생횟수가 같으면 고유 번호가 낮은 순으로 수록
# 장르 당 최대 두개까지만 수록

def mysolution(genres, plays):
    album = {}
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]

        if genre in album:
            album[genre].append((play, i))
        else:
            album[genre] = [(play, i)]

    top_genre_list = []
    for key, value in album.items():
        top_genre_list.append( (sum(i[0] for i in value), key) )
    top_genre_list.sort(reverse=True) # pop, classic 순으로 정렬완료

    # return top_genre_list

    result = []
    for _, genre in top_genre_list:
        album[genre].sort(reverse=True) # pop 안에서도 재생횟수로 정렬완료

        for item in album[genre][:2]: # 장르당 최대 두개까지 수록
            result.append(item[1])
    # return album
    
    return result

# 런타임 에러가 뜸

from collections import defaultdict

def solution(genres, plays):
    answer = []

    genres_order = defaultdict(int)
    genres_plays = defaultdict(list)

    for i, (genre, play) in enumerate(zip(genres, plays)): # 리스트 두개를 zip으로 튜플로 만들어서, enumerate로 고유값 넣어서 for문 돌리기
        genres_order[genre] += play # 장르별 재생 횟수 합
        genres_plays[genre].append((i, play)) # 번호, 재생횟수 쌍 리스트

    for genre, _ in sorted(genres_order.items(), key=lambda x: x[1], reverse=True): # 재생횟수 가장 많은 장르부터
        for i, play in sorted(genres_plays[genre], key=lambda x:x[1], reverse=True)[:2]:
            answer.append(i)

    return answer
