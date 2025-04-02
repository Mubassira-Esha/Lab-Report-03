def is_safe(graph, color, v, c):
    
    for i in range(len(graph)):
        if graph[v][i] == 1 and color[i] == c:
            return False
    return True

def graph_coloring_util(graph, color, v, k):
   
    if v == len(graph):
        return True

   
    for c in range(1, k + 1):
        if is_safe(graph, color, v, c):
            color[v] = c

           
            if graph_coloring_util(graph, color, v + 1, k):
                return True

         
            color[v] = 0

    return False

def graph_coloring(graph, k):
    color = [-1] * len(graph)

    if graph_coloring_util(graph, color, 0, k):
        return color
    else:
        return None

def main():
   
    n, m, k = map(int, input().split())
    
    graph = [[0 for _ in range(n)] for _ in range(n)]

    for _ in range(m):
        u, v = map(int, input().split())
        graph[u][v] = 1
        graph[v][u] = 1

    result = graph_coloring(graph, k)
    if result:
        print(f"Coloring Possible with {k} Colors")
        print(f"Color Assignment: {result}")
    else:
        print(f"Coloring Not Possible with {k} Colors")

if __name__ == "__main__":
    main()
