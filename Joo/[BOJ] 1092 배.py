import sys

N = int(sys.stdin.readline())
cranes = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
boxes = list(map(int, sys.stdin.readline().split()))

cranes.sort(reverse=True)
boxes.sort(reverse=True)

if cranes[0] < boxes[0]:
    print(-1)
    exit()

time = 0

while len(boxes) > 0:
    for crane in cranes:
        # 하도 시간초과 나서 넣어준 코드.. 남은 박스의 최소 무게보다 크레인 무게가 더 작으면 그냥 넘어가기
        if boxes and crane < boxes[-1]:
            continue
        for box in boxes:
            if crane >= box:
                boxes.remove(box)
                break
    time += 1
print(time)