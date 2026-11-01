from collections import deque

def bfs(graph, x, y, moves):
    i = x
    j = y
    ans = []

    visited = []
    queue = deque()
    visited.append((i, j))
    queue.append((i, j))

    while queue:
        current = queue.popleft()
        ans.append(current)

        for move in moves:
            ni = i+move[0]
            nj = j+move[1]
            if (ni, nj) not in visited and ni>=0 and nj>=0 and ni<len(graph) and nj<len(graph[0]):
                visited.append((ni, nj))
                queue.append((ni, nj))

    return ans


def main():
    pass

    graph = [[0] * 5 for _ in range(5)]
    moves = [(1, 0, "D"), (0, 1, "R"), (-1, 0, "U"), (0, -1, "L")]

    counter = 0
    for i in range(5):
        for j in range(5):
            counter +=1
            graph[i][j] = counter

    x = 2
    y = 2

    res = bfs(graph, x, y, moves)

    for x,y in res:
        print(graph[x][y])

if __name__ == '__main__':
    main()