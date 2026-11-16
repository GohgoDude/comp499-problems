#import sys,io
from collections import deque
#def test(s): sys.stdin=io.StringIO(s); main()

def bfs(people, adj, max_impostors):
    nodeCounts = [0] * (people+1)
    queue = deque()

    for i in range(1, people+1):
        visited = [False] * (people+1)
        queue.append(i)
        visited[i] = True
        nodeCount = 1

        while queue:
            u = queue.pop()

            for x in adj[u]:
                if not visited[x]:
                    visited[x] = True
                    queue.append(x)
                    nodeCount += 1
        nodeCounts[i] = nodeCount
    
    verdict = []
    for node in nodeCounts[1:]:
        if node <= max_impostors:
            verdict.append(0)
        else:
            verdict.append(1)
    return verdict

def get_adj_list(people, edges):
    adj_mtx = {}
    for i in range(people):
        adj_mtx[i+1] = []
    for u, v in edges:
        #backwards edges
        adj_mtx[v].append(u)
    return adj_mtx

def main():
    people, max_impostors = map(int, input().split())
    edges = []
    for i in range(people):
        current = list(map(int, input().split()))
        if current[0] == 0:
            continue
        else:
            for j in current[1:]:
                edges.append([i+1, j])

    adj_list = get_adj_list(people, edges)
    res = bfs(people, adj_list, max_impostors)
    for num in res:
        print(num)

# test("""4 1
# 2 2 3
# 1 3
# 3 4 2 1 
# 0
# """)

# test("""4 1
# 1 2
# 1 1
# 1 3
# 1 4
# """)

# test("""4 2
# 1 2
# 1 3
# 0
# 0
# """)

# test("""3 1
# 0
# 1 2
# 0
# """)


if __name__ == '__main__':
    main()