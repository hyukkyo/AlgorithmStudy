# DFS, BFS 둘다 할 수 있음.

# DFS의 시간복잡도는 O(V+E) 완전탐색


def canVisitAllRooms(rooms):
    visited = [False] * len(rooms)
    visited[0] = True

    # cur_v에 연결된 모든 vertex에 방문한다.
    def dfs(cur_v):
        visited[cur_v] = True
        for next_v in rooms[cur_v]:
            if visited[next_v] == False:
                dfs(next_v)

    dfs(0)

    return all(visited)


print(canVisitAllRooms([[1],[2],[3],[]]))