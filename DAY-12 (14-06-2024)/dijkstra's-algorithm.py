def dijkstra(d,n):
    visited = [False]*n
    distance = [float('inf')]*n
    distance[d] = 0
    for _ in range(n):
        min_dist = float('inf')
        min_index = -1
        for i in range(n):
            if not visited[i] and distance[i] < min_dist:
                min_dist = distance[i]
                min_index = i
                visited[min_index] = True
                for i in range(n):
                    if not visited[i] and graph[min_index][i] != 0 and distance[min_index]:
                        new_dist = distance[min_index] + graph[min_index][i]
                        if new_dist < distance[i]:
                            distance[i] = new_dist
    return distance
n = int(input("Enter the number of nodes: "))
graph = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        graph[i][j] = int(input(f"Enter the weight of edge from node {i}"))
n = int(input("Enter the source node: "))
print(dijkstra(graph,n))
print(graph)
                                # Output