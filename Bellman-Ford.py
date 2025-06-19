from collections import deque

t = int(input())

for _ in range(t):
    n, m, w = map(int, input().split())
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        s, e, t = map(int, input().split())
        graph[s].append((e, t))
        graph[e].append((s, t))

    for _ in range(w):
        s, e, t = map(int, input().split())
        graph[s].append((e, -t))

    def spfa():
        dist = [0] * (n + 1)
        in_queue = [True] * (n + 1)
        count = [0] * (n + 1)
        q = deque(range(1, n + 1))

        while q:
            u = q.popleft()
            in_queue[u] = False

            for v, cost in graph[u]:
                if dist[v] > dist[u] + cost:
                    dist[v] = dist[u] + cost
                    count[v] += 1
                    if count[v] >= n:
                        return True
                    if not in_queue[v]:
                        q.append(v)
                        in_queue[v] = True
        return False

    print("YES" if spfa() else "NO")
