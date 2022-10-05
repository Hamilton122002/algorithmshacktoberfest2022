from queue import PriorityQueue
v = 14
graph = [[] for i in range(v)]

def bestfirst(source, target, n):
    visited = [False] * n
    pq = PriorityQueue()
    pq.put((0, source))
    while pq.empty() == False:
        u = pq.get()[1]
        print(u, end=" ")
        visited[u] = True
        if u == target:
            break

        for v, c in graph[u]:
            if visited[v] == False:
                visited[v] == True
                pq.put((c, v))
    print()

def edge(x, y, cost):
    graph[x].append((y, cost))
    graph[y].append((x, cost))
edge(0, 1, 3)
edge(0, 2, 6)
edge(0, 3, 5)
edge(1, 4, 9)
edge(1, 5, 8)
edge(2, 6, 12)
edge(2, 7, 14)
edge(3, 8, 7)
edge(8, 9, 5)
edge(8, 10, 6)
edge(9, 11, 1)
edge(9, 12, 10)
edge(9, 13, 2)

source = 0
target = 12

print(f"Source: {source}, Destination: {target}")
print("The path is as follows")
bestfirst(source, target, v)