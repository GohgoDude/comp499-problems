from math import inf
import heapq
import sys,io
#def test(s): sys.stdin=io.StringIO(s); main()

def adjacency_list_dictionary(N, edges):
    adjacency_list = {}
    for i in range(N):
        adjacency_list[i+1] = []

    for edge in edges:
        path, w = edge
        adjacency_list[path[0]].append((path[1], w))
    return adjacency_list

def main():
    N,M = map(int, input().split())

    edges = []

    for _ in range(M):
        a, b, w = map(int, input().split())
        edges.append(([a, b], w))

    #print(edges)
    adjacency_list = adjacency_list_dictionary(N, edges)
    #print(adjacency_list)

    dist = [inf] * (N+1)
    dist[1] = 0
    heap = [(0,1)]

    while heap:
        d, u = heapq.heappop(heap)
        # if d >= dist[u]:
        #     continue
        for v, w in adjacency_list[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))

    if dist[N] == inf:
        print("IMPOSSIBLE")
    else:
        print(dist[N])


# test("""4 5
# 1 2 6
# 1 3 1
# 3 2 1
# 2 4 2
# 3 4 7
# """)

# test("""3 1
# 2 1 5
# """)

if __name__ == '__main__':
    main()