import sys, io
from collections import deque
# def test(s): sys.stdin=io.StringIO(s); main()

def explore(graph, start):
    moves = [(0, -1, 'L'), (-1, 0, 'U'), (0, 1, 'R'), (1, 0, 'D')]
    parent = {start:None}

    queue = deque()
    queue.append(start)

    while queue:
        current = queue.popleft()
        if graph[current[0]][current[1]] == 'B':
            solution = []
            while parent[current] != None:
                path = parent[current]
                solution.append(path[2])
                current = (path[0], path[1])
            solution = "".join(solution[::-1])
            return solution

        for move in moves:
            nr = current[0] + move[0]
            nc = current[1] + move[1]
            if nr >=0 and nc >= 0 and nc < len(graph[0]) and nr < len(graph) and graph[nr][nc] != '#' and (nr,nc) not in parent:
                parent[(nr,nc)] = (current[0],current[1],move[2])
                queue.append((nr, nc))

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
                start = (i, j)

    res = explore(graph, start)

    if len(res) > 0:
        print("YES")
        print(len(res))
        print(res)
    else:
        print("NO")

# test("""5 8
# ########
# #.A#...#
# #.##.#B#
# #......#
# ########
# """)

# test("""1 3
# A#B
# """)

if __name__ == '__main__':
    main()