def minpath(n, edges, A, B):
    graph = [[] for i in range(n)]
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    dist = [float('inf')] * n
    used = [False] * n
    dist[A] = 0
    for i in range(n):
        u = -1
        for j in range(n):
            if not used[j] and (u == -1 or dist[j] < dist[u]):
                u = j
        if u == -1 or dist[u] == float('inf'):
            break
        used[u] = True
        for v, w in graph[u]:
            newdist = max(dist[u], w)
            if newdist < dist[v]:
                dist[v] = newdist
    if dist[B] == float('inf'):
        return -1
    return dist[B]