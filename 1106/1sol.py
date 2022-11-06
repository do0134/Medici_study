from collections import deque

def bfs(s):
    q = deque()
    q.append(s)
    visit = list()
    while q:
        start = q.popleft()
        for i in range(n):
            if adj[start][i] == 1 and i not in visit:
                visit.append(i)
                v[start][i] = 1
                q.append(i)
    for j in visit:
        v[s][j] = 1


n = int(input())
adj = [list(map(int,input().split())) for _ in range(n)]
v = [[0]*n for _ in range(n)]

for i in range(n):
    bfs(i)

for i in v:
    print(*i)