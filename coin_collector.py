import sys,io

def test(s): sys.stdin=io.StringIO(s); main()

def dfs(rooms, adj_list):
    colors = [0] * (rooms+1)
    stack = [(1, adj_list[1])]
    colors[1] = 1
    res = []

    while stack:
        v, neighbors = stack.pop()
        if len(neighbors) == 0:
            colors[v] = 2
            res.append(v)
        else:
            u = neighbors.pop()
            if colors[u] == 0:
                colors[u] = 1
                stack.append((v, neighbors))
                stack.append((u, adj_list[u]))
            elif colors[u] == 1:
                stack.append((v, neighbors))
    return res



def adjacency_list_dictionary(rooms, edges):
    adj_list = {}
    for i in range(rooms):
        adj_list[i+1] = []
    for edge in edges:
        v1, v2 = edge
        adj_list[v1].append(v2)
    return adj_list


def main():
    rooms, tunnels = map(int, input().split())
    room_values = list(map(int, input().split()))

    edges = []
    edges_r = []
    for _ in range(tunnels):
        a, b = map(int, input().split())
        edges.append([a, b])
        edges_r.append([b, a])

    adj_list = adjacency_list_dictionary(rooms, edges)
    adj_list_r = adjacency_list_dictionary(rooms, edges_r)

    print(adj_list)
    result = dfs(rooms, adj_list)
    print(result)
    

    

test("""4 4
4 5 2 7
1 2
2 1
1 3
2 4
""")

test("""5 5
10 6 4 7
1 2
1 5
2 3
3 1
3 4
""")

# if __name__ == '__main__':
#     main()