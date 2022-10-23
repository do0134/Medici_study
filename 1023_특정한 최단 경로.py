import heapq
import sys

N, E = map(int, input().split())
arr = [[] for _ in range(N + 1)]
result = []

for e in range(E):
    a, b, c = map(int, sys.stdin.readline().split())

    arr[a].append([b, c])
    arr[b].append([a, c])

u, v = map(int, input().split())


def dijsktra(start, end):
    distance = [int(10e9)] * (N + 1)
    distance[start] = 0

    q = []
    # 최소 값을 빠르게 찾기 위해 heapq 사용
    # => Python heap은 최소 힙(min heap)

    # 처음에 생각없이 index를 앞으로 넣음
    # 성공은 했으나 시간이 굉장히 커 분석
    # 결과적으로 모든 node를 찾아다녔기에 성공했지만
    # heapq 정렬이 node를 기준으로 되어있어
    # 정작 원하는 최소 거리를 가져오지 못하는 상황이 되었음
    # heapq.heappush(q, [start, distance[start]])
    # while q:
    #     #
    #     now, dis = heapq.heappop(q)
    #     for link, dis in arr[now]:
    #         cost = distance[now] + dis
    #         if cost < distance[link]:
    #             distance[link] = cost
    #             heapq.heappush(q, [link, cost])

    # 수정안 => 시간이 절반으로 감소
    heapq.heappush(q, [distance[start], start])
    while q:
        dist, now = heapq.heappop(q)
        for link, dis in arr[now]:
            cost = distance[now] + dis
            if cost < distance[link]:
                distance[link] = cost
                heapq.heappush(q, [cost, link])

    return distance[end]

# 경로 1 => 1 -> u -> v -> N
sol1 = dijsktra(1, u) + dijsktra(u, v) + dijsktra(v, N)
# 경로 2 => 1 -> v -> u -> N
sol2 = dijsktra(1, v) + dijsktra(u, v) + dijsktra(u, N)

print(-1) if min(sol1, sol2) >= int(10e9) else print(min(sol1, sol2))
