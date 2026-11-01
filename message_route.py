from collections import deque
import sys, io
def test(s): sys.stdin=io.StringIO(s); main()

def bfs(adj, src, computers):
    parent = {}
    q = deque()

    parent[src] = None
    q.append(src)

    while q:
        curr = q.popleft()

        if curr == computers:
            res = []
            while curr != None:
                prev = parent[curr]
                res.append(curr)
                curr = prev
            return res[::-1]

        # visit all the unvisited
        # neighbours of current node
        for x in adj[curr]:
            if x not in parent:
                parent[x] = curr
                q.append(x)


def adjacency_list_dictionary(vertices, edges):
    adjacency_list = {}
    # Add vertices to the dictionary
    for v in vertices:
        adjacency_list[v] = []
    # Add edges to the dictionary
    for edge in edges:
        vertex1, vertex2 = edge
        adjacency_list[vertex1].append(vertex2)
        adjacency_list[vertex2].append(vertex1)
    # Display the adjacency list
    # for vertex, neighbors in adjacency_list.items():
    #     print(f"{vertex} -> {' '.join(map(str, neighbors))}")
    return adjacency_list


def main():
    computers, links = map(int, input().split())

    edges = []
    vertices = set()

    for _ in range(links):
        a, b = map(int, input().split())
        vertices.add(a)
        vertices.add(b)
        edges.append([a, b])

    if 1 not in vertices:
        print("IMPOSSIBLE")
        return

    # print(edges)
    # print(vertices)

    adjacency_list = adjacency_list_dictionary(vertices, edges)
    print("adjacency list: ")
    print(adjacency_list)

    #print(adjacency_list[1])

    ans = bfs(adjacency_list, 1, computers)

    if ans:
        print(len(ans))
        print(" ".join(map(str, ans)))
    else:
        print("IMPOSSIBLE")

test("""5 5
1 2
1 3
1 4
2 3
5 4
""")

# test("""4 2
# 1 2
# 3 4
# """)

# if __name__ == '__main__':
#     main()