def dfs(adjacency_list, tasks):
    colors = [0] * (tasks+1)
    res = []

    for i in range(tasks):
        if colors[i+1] != 2:
            stack = [(i+1, adjacency_list[i+1])]
    
            while stack:
                v, neighbors = stack.pop()
                colors[v] = 1
                if len(neighbors) == 0:
                    colors[v] = 2
                else:
                    u = neighbors.pop()
                    if colors[u] == 0:
                        colors[u] = 1
                        stack.append((v, neighbors))
                        stack.append((u, adjacency_list[u]))
                    elif colors[u] == 1:
                        return []
                    else:
                        stack.append((v, neighbors))
                if colors[v] == 2:
                    res.append(v)
    return res[::-1]

def adjacency_list_dictionary(tasks, edges):
    adjacency_list = {}
    for i in range(tasks):
        adjacency_list[i+1] = []
    
    for edge in edges:
        vertex1, vertex2 = edge
        adjacency_list[vertex1].append(vertex2)
    return adjacency_list

def main():
    tasks, prerequisites = map(int, input().split())
    edges = []

    for _ in range(prerequisites):
        edges.append(list(map(int, input().split())))
    
    adjacency_list = adjacency_list_dictionary(tasks, edges)
    res = dfs(adjacency_list, tasks)

    if len(res) > 0:
        print(" ".join(str(num) for num in res))
    else:
        print("IMPOSSIBLE")

if __name__ == '__main__':
    main()