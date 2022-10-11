from collections import deque
dr = [1,-1,0,0]
dc = [0,0,1,-1]


def solution(board):
    n = len(board)
    v = [[[int(1e9)] * n for _ in range(n)] for ha in range(4)]
    q = deque()
    q.append((0,0,-1))
    for i in range(4):
        v[i][0][0] = 0


    while q:
        cr,cc,dir = q.popleft()
        if dir == -1:
            for d in range(4):
                nr = cr+dr[d]
                nc = cc+dc[d]
                if 0 <= nr < n and 0 <= nc < n and board[nr][nc] != 1 :
                    v[d][nr][nc] = 100
                    q.append((nr,nc,d))
        else:
            for d in range(4):
                nr = cr+dr[d]
                nc = cc+dc[d]
                if nr == 0 and nc == 0 :
                    continue
                elif 0 <= nr < n and 0 <= nc < n and board[nr][nc] != 1:
                    if dir == d:
                        if v[d][nr][nc] > v[d][cr][cc]+100 :
                            v[d][nr][nc] = v[d][cr][cc]+100
                            q.append((nr,nc,d))
                    else:
                        if v[d][nr][nc] > v[dir][cr][cc]+600:
                            v[d][nr][nc] = v[dir][cr][cc]+600
                            q.append((nr,nc,d))

    min_v = int(1e9)
    for i in range(4):
        min_v = min(min_v,v[i][n-1][n-1])
    return min_v