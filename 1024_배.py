import sys

N = int(input())
tools = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)

M = int(input())
boxs = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)

# Cranes 중 들 수 있는 가장 무거운 무게보다
# Boxs 중 가장 무거운 게 더 무거우면
# 어떠한 경우에도 옮기지 못하는 것이 1개 이상 존재함으로
# 이 때 -1 출력
if boxs[0] > tools[0]:
    print(-1)

else:
    # 시간을 측정하는 변수
    time = 0
    # 모든 박스를 옮길 때까지
    while len(boxs):
        # Cranes들을 돌면서
        for tool in tools:
            # 남은 박스가 없으면 break
            if not len(boxs):
                break

            # 현재 Crane이 가장 가벼운 box를 못들면 바로 빠져나가기
            # 시간 줄이기 위한 방법
            elif tool < boxs[-1]:
                break

            # 박스들을 무거운 것들부터 옮기면서
            # Crane이 들 수 있는 Box를 발견하면
            # 해당 Box가 있는 index를 pop한다
            else:
                for i in range(len(boxs)):
                    if tool >= boxs[i]:
                        boxs.pop(i)
                        break

        # 모든 Cranes를 돌 때마다 time + 1
        time += 1

    print(time)
