import sys, io
def test(s): sys.stdin=io.StringIO(s); main()

def dfs(start, adjacency_list, vertices):
    stack = [(start, adjacency_list)]
    colors = [0] * len(vertices)+1
    
    while stack:
        v, neighbors = stack.pop()
        if len(neighbors) == 0:
            colors[v] = 2
        else:
            u = neighbors.pop()
            if colors[u] == 0:
                colors[u] = 1
                stack.push(u, adjacency_list[u])
            elif colors[u] == 1:
                return []



def adjacency_list_dictionary(vertices, edges):
    adjacency_list = {}
    for vertex in vertices:
        adjacency_list[vertex] = []
    
    for edge in edges:
        vertex1, vertex2 = edge
        adjacency_list[vertex1].append(vertex2)
    return adjacency_list

def main():
    tasks, prerequisites = map(int, input().split())
    vertices = set()
    edges = []
    for _ in range(prerequisites):
        a, b = map(int, input().split())
        vertices.add(a)
        vertices.add(b)
        edges.append([a, b])
    
    adjacency_list = adjacency_list_dictionary(vertices, edges)

    res = dfs(1, adjacency_list, vertices)

    #print(edges)
    #print(vertices)
    print(adjacency_list)


test("""5 4
1 3
2 3
3 4
2 5
""")

test("""3 3
1 2
2 3
3 1
""")

# if __name__ == '__main__':
#     main()