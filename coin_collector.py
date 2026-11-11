import sys,io

def test(s): sys.stdin=io.StringIO(s); main()

def controlled_dfs(rooms, adj_list, filter):
    neighbor_list = {}
    for i in range(len(adj_list)):
        neighbor_list[i+1] = adj_list[i+1].copy()

    res = []
    colors = [0] * (rooms+1)
    count = 0
    for i in range(len(filter)):
        if colors[filter[i]] == 2:
            continue
        count += 1
        stack = [(filter[i], neighbor_list[filter[i]])]
        colors[filter[i]] = 1

        while stack:
            v, neighbors = stack.pop()
            if len(neighbors) == 0:
                colors[v] = 2
                res.append((count, v))
            else:
                u = neighbors.pop()
                if colors[u] == 0:
                    colors[u] = 1
                    stack.append((v, neighbors))
                    stack.append((u, neighbor_list[u]))
                elif colors[u] == 1 or colors[u] == 2:
                    stack.append((v, neighbors))
    return res, count

def dfs(rooms, adj_list):
    neighbor_list = {}
    for i in range(len(adj_list)):
        neighbor_list[i+1] = adj_list[i+1].copy()

    colors = [0] * (rooms+1)
    stack = [(1, neighbor_list[1])]
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
                stack.append((u, neighbor_list[u]))
            elif colors[u] == 1 or colors[u] == 2:
                stack.append((v, neighbors))
    return res[::-1]

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

    #print(adj_list)
    result = dfs(rooms, adj_list)

    scc, count = controlled_dfs(rooms, adj_list_r, result)

    
    print(scc)
    

test("""10 13
3 3 4 3 3 3 3 5 6 10
1 2
2 3
3 1
1 8
8 9
9 8
9 10
1 4
4 5
5 10
5 6
6 7
7 4
""")


# test("""4 4
# 4 5 2 7
# 1 2
# 2 1
# 1 3
# 2 4
# """)

# test("""5 5
# 10 6 4 7
# 1 2
# 1 5
# 2 3
# 3 1
# 3 4
# """)

# test("""5 5
# 3 7 4 6 9
# 1 2
# 1 3
# 3 4
# 2 4
# 2 5
# """)

# test("""5 6
# 4 8 7 2 5
# 1 3
# 1 5
# 3 4
# 4 2
# 2 1
# 2 5
# """)

# if __name__ == '__main__':
#     main()