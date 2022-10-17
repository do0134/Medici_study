def solution(enroll, referral, seller, amount):  # enroll : 판매원 리스트, referral : 각 판매원을 가입시킨 판매원, seller : 실제로 판 사람, amount : 판 양
    answer = []
    # 각 판매원의 이익 dictionary 만들기
    count = {"minho": 0}
    # 부모 dictionary 만들기
    parent = {"minho": "minho"}
    for i in range(len(enroll)):
        count[enroll[i]] = 0
        if referral[i] == "-":
            parent[enroll[i]] = "minho"
            continue
        parent[enroll[i]] = referral[i]
    for i in range(len(seller)):
        person = seller[i]
        cost = amount[i] * 100
        while True:
            count[person] += cost - int(cost * 0.1)
            if person == parent[person]:  # 민호까지 갔으면 break
                break
            person = parent[person]
            cost = int(cost * 0.1)
            if cost == 0:  # 줄 돈 없으면 break
                break
    for pp in enroll:
        answer.append(count[pp])

    return answer