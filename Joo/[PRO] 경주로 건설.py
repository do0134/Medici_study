# DP
import sys
import collections
def solution(board):
    INF = sys.maxsize
    N = len(board)
    answer = INF
    dd = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    dist = [[[INF for _ in range(N)] for _ in range(N)] for _ in range(4)]  # 값을 넣어줄 3차원 리스트, N * N 리스트가 4개가 있는거! 각 방향별로 !
    q = collections.deque()
    q.append((0, 0, 0, 0))  # x, y, cost, d(방향)
    q.append((0, 0, 0, 1))
    while q:
        x, y, cost, d = q.popleft()
        for i in range(4):
            nx, ny = x + dd[i][0], y + dd[i][1]
            if 0 <= nx < N and 0 <= ny < N and not board[nx][ny]:
                ncost = cost + 1
                # 만약에 방향이 다르면 5를 더 더해줌
                if d != i:
                    ncost += 5
                # 지금 적혀있는 cost보다 현재 cost가 더 적으면 값 업데이트
                if dist[i][nx][ny] > ncost:
                    dist[i][nx][ny] = ncost
                    # 마지막 칸이면 queue에 안넣고 continue
                    if nx == N-1 and ny == N-1:
                        continue
                    q.append((nx, ny, ncost, i))
    # 각 방향별로 최소 cost가 적혀있는데 그 cost 중 최소값 찾으면 답!!
    for i in range(4):
        answer = min(answer, dist[i][N-1][N-1])
    return answer * 100
