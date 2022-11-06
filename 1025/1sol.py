import sys

n = int(input())
crane = list(map(int,sys.stdin.readline().split()))
m = int(input())
box = list(map(int,sys.stdin.readline().split()))

crane.sort(reverse = True)
box.sort(reverse = True)

if crane[0] < box[0] :
    print(-1)
else:
    cnt = 0
    while box:
        cnt += 1
        for i in range(n):
            for j in box:
                if not box:
                    break
                if crane[i] < box[-1]:
                    break
                if crane[i] >= j:
                    box.remove(j)
                    break
    print(cnt)
