N = int(input())

arr = [[0] * N for _ in range(N)]

for n in range(N):
    node = list(map(int, input().split()))
    for index in range(N):
        if node[index] == 1:
            arr[n][index] = 1

while True:
    flag = 0
    for a in range(N):
        for b in range(N):
            for c in range(N):
                if arr[a][b] == 1 and arr[b][c] == 1 and arr[a][c] == 0:
                    arr[a][c] = 1
                    flag = 1
    if not flag:
        break

for n in range(N):
    print(*arr[n])