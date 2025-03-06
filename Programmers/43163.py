from collections import deque

def bfs(graph, start):
    visited = [False] * len(graph)
    q = deque()
    q.append([start])
    visited[start] = True
    count = 1

    while q:
        v = q.popleft()
        for neighbor in graph[v]:
            if not visited[neighbor]:
                q.append(neighbor)
                visited[neighbor] = True
                count += 1
    return count

    

def solution(begin, target, words):
    answer = 0
    if target not in words: # 타겟 단어가 words에 없으면 0을 반환
        return 0

    # 일단 주어진 words를 인접 리스트 형식으로 변환해야 함
    words.append(begin) # 시작점도 추가하기
    graph = [[] for _ in range(len(words))]

    for i, word in enumerate(words):
        for j, compared in enumerate(words):

            count = 0
            for c in range(len(word)):
                if word[c] != compared[c]: # 스펠링이 다른 갯수를 센다
                    count += 1
            if count == 1: # 한글자만 다르면 노드를 연결
                graph[i].append(j)
    # print(graph)
    q = deque()
    visited = [0] * len(graph)
    q.append(len(graph)-1)
    visited[len(graph)-1] = 1

    while q:
        v = q.popleft()

        if words[v] == target:
            answer = visited[v] - 1
            break
        
        for neighbor in graph[v]:
            if visited[neighbor] == 0:
                visited[neighbor] = visited[v] + 1
                q.append(neighbor)

    return answer