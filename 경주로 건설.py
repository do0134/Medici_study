from collections import deque


# def solution(board):
#     answer = 10 ** 9
#     length = len(board)

#     ey, ex = length, length
#     direction = [0, 0]

#     d = [[0, 1], [1, 0], [0, -1], [-1, 0]]

#     def build(y, x, price, where):
#         nonlocal answer, direction
#         if y == ey - 1 and x == ex - 1:
#             answer = min(answer, price)

#         elif price >= answer:
#             pass

#         else:
#             new_price = price + 100
#             for my, mx in d:
#                 ny, nx = y + my, x + mx
#                 if 0 <= ny < length and 0 <= nx < length and not board[ny][nx]:
#                     board[ny][nx] = 2
#                     if where == [0, 0] or abs(where[0]) == abs(my) and abs(where[1]) == abs(mx):
#                         new_where = [my, mx]
#                         build(ny, nx, new_price, new_where)

#                     else:
#                         new_where = [my, mx]
#                         build(ny, nx, new_price + 500, new_where)
#                     board[ny][nx] = 0

#                 else:
#                     continue

#     board[0][0] = 1
#     build(0, 0, 0, direction)

#     return answer


# def solution(board):
#     length = len(board)
#     dp = [[[1000] * 4] * length for _ in range(length)]
#     d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
#
#     arr = deque()
#     arr.append([0, 0, 0, 0])
#     arr.append([0, 0, 0, 1])
#     while arr:
#         ny, nx, nm, look = arr.popleft()
#         for di in range(4):
#             my, mx = ny + d[di][0], nx + d[di][1]
#             if 0 <= my < length and 0 <= mx < length and not board[my][mx]:
#                 mm = nm + 100
#                 if di != look:
#                     mm += 500
#                 if dp[my][mx][di] > mm:
#                     dp[my][mx][di] = mm
#                     if my != length - 1 or mx != length - 1:
#                         arr.append([my, mx, mm, dp[my][mx][di]])
#
#     return min(dp[length - 1][length - 1])
#     # x, y 순서가 바뀌면 값이 변함. 이유가 뭘까


def solution(board):
    result = 10000
    n = len(board)
    direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    dp = [[[10000] * 4 for i in range(n)] for j in range(n)]
    queue = deque()
    queue.append([0, 0, 0, 0])
    queue.append([0, 0, 0, 1])
    while queue:
        x, y, m, d = queue.popleft()
        for i2 in range(4):
            new_x = x + direction[i2][0]
            new_y = y + direction[i2][1]
            if -1 < new_x < n and -1 < new_y < n and board[new_x][new_y] == 0:
                new_m = m + 100
                if not d == i2:
                    new_m += 500
                if new_m < dp[new_x][new_y][i2]:
                    dp[new_x][new_y][i2] = new_m
                    if new_x == n - 1 and new_y == n - 1:
                        continue
                    queue.append([new_x, new_y, new_m, i2])

    result = min(dp[n - 1][n - 1])
    return result * 100
