from collections import deque

# 최단거리 문제는 BFS로 푸는게 좋다.

def shortestPathBinaryMatrix(grid):
    shortest_path_len = -1
    n = len(grid)

    if grid[0][0] != 0 or grid[n-1][n-1] != 0:
        return shortest_path_len
    
    dx = [1, -1, 0, 0, 1, -1, 1, -1]
    dy = [0, 0, 1, -1, 1, -1, -1, 1]

    queue = deque()
    queue.append((0, 0, 1))
    visited = [[False]*n for _ in range(n)]
    visited[0][0] = True

    while queue:
        cur_x, cur_y, cur_len = queue.popleft()
        # 목적지에 도착했을 때 cur_len을 반환
        if cur_x == n-1 and cur_y == n-1:
            shortest_path_len = cur_len
            break

        for i in range(8):
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]

            if next_x >= 0 and next_x < n and next_y >= 0 and next_y < n:
                if grid[next_x][next_y] == 0 and not visited[next_x][next_y]:
                    queue.append((next_x, next_y, cur_len + 1))
                    visited[next_x][next_y] = True


    return shortest_path_len


print(shortestPathBinaryMatrix([[0,1],[1,0]]))