import sys, io
from collections import deque
# def test(s): sys.stdin=io.StringIO(s); main()

def explore(graph, start):
    row = start[0]
    col = start[1]
    moves = [(0, -1, 'L'), (-1, 0, 'U'), (0, 1, 'R'), (1, 0, 'D')]
    visited = []
    ans = []

    queue = deque()
    visited.append((row, col))
    queue.append((row, col))

    while queue:
        
        current, parent = queue.popleft()
        ans.append((current, parent))
        if graph[current[0]][current[1]] == 'B':
            solution = ""
            current, parent = ans[-1]
            for i in range(len(ans)-2, -1, -1):
                ncurrent, nparent = ans[i]
                if ncurrent[0] == parent[0] and ncurrent[1] == parent[1]:
                    solution += current[2]
                    current, parent = ncurrent, nparent
                else:
                    continue
            print(ans[1:])
            return solution[::-1]

        for move in moves:
            nr = current[0] + move[0]
            nc = current[1] + move[1]
            if nr >=0 and nc >= 0 and nc < len(graph[0]) and nr < len(graph) and graph[nr][nc] != '#' and (nr,nc) not in visited:
                visited.append((nr, nc))
                parent = (current[0], current[1])
                queue.append(((nr, nc, move[2]), (current[0], current[1])))

    return ""
    
def main():
    N,M = map(int, input().split())

    graph = [["."] * M for _ in range(N)]

    start = (0,0)

    for i in range(N):
        line = input()
        for j in range(M):
            graph[i][j] = line[j]
            if line[j] == 'A':
                start = ((i, j), None)

    res = explore(graph, start)

    res_len = len(res)

    if res_len > 0:
        print("YES")
        print(res_len)
        print(res)
    else:
        print("NO")

if __name__ == '__main__':
    main()