import heapq
def minpath(n, edges, A, B):
    graph = [[] for i in range(n)]
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    dist = [float('inf')] * n
    used = [False] * n
    dist[A] = 0
    heap = [(0, A)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        if u == B:
            return d
        for v, w in graph[u]:
            newdist = max(d, w)
            if newdist < dist[v]:
                dist[v] = newdist
                heapq.heappush(heap, (newdist, v))
        return -1
    return dist[B]