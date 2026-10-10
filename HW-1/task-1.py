def minpath(n, edges, A, B):
    graph = [[] for i in range(n)]
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    #навскидку в графе расстояния до 10^7, грубо, но ладно)
    dist = [10**7] * n
    used = [False] * n
    dist[A] = 0
    for i in range(n):
        u = -1
        for j in range(n):
            if not used[j] and (u == -1 or dist[j] < dist[u]):
                u = j
        if u == -1 or dist[u] == 10**18:
            break
        used[u] = True
        for v, w in graph[u]:
            newdist = max(dist[u], w)
            if newdist < dist[v]:
                dist[v] = newdist
    if dist[B] == 10**7:
        return -1
    return dist[B]