def solution(enroll, referral, seller, amount):
    master = dict()
    get_money = dict()
    # 센터는 미리 입력
    get_money['-'] = 0

    for idx in range(len(enroll)):
        # 각 조직원들을 초기화
        get_money[enroll[idx]] = 0
        # 추천인을 받아놓음 => dict으로 받아 빠르게 검색할 수 있도록
        master[enroll[idx]] = referral[idx]

    # 판매원들
    for idx1 in range(len(seller)):
        # 번 돈 추가
        get_money[seller[idx1]] += amount[idx1] * 100
        # now: 현재 파악하는 조직원
        now = seller[idx1]
        # 얻은 이익의 10%가 이익
        tip = (amount[idx1] * 100) // 10
        while True:
            # tip이 1보다 작거나, 본인이 center이면 break
            if tip < 1 or now == '-':
                break
            else:
                # 상납금 계산
                get_money[now] -= tip
                get_money[master[now]] += tip
                # 새로 파악할 조직원
                now = master[now]
                # 팁은 받은 금액에 대해서만 10%
                tip //= 10

    # dict들의 value(이익금)만 list로 뽑아내기
    # center는 제외해야하므로 [1:]
    answer = list(get_money.values())[1:]

    return answer


print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
               ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
               ["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10]))
