def city_best(n, edges, mileage):
    graph = [[] for i in range(n)]
    for a, b, distance in edges:
        graph[a].append((b, distance))
        graph[b].append((a, distance))
    best = 0
    max_count = -1
    for start in range(n):
        dist = [float('inf')] * n
        used = [False] * n
        dist[start] = 0




        for i in range(n):
            u = -1
            for j in range(n):
                if not used[j] and (u == -1 or dist[j] < dist[u]):
                    u = j


            if u == -1 or dist[u] == float('inf'):
                break
            used[u] = True
            for v, w in graph[u]:
                newdist = dist[u] + w
                if newdist < dist[v]:
                    dist[v] = newdist
        count = 0
        for j in range(n):
            if j != start and dist[j] <= mileage:
                count += 1
        if count > maxcount:
            maxcount = count
            best = start
    return best