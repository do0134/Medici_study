function solution(enroll, referral, seller, amount) {
  const money = {}; // 이름: 액수
  const parents = {}; // 이름: 부모

  enroll.forEach((e, i) => {
    money[e] = 0; // 초기 액수 0
    parents[e] = referral[i]; // 부모 정해주기
  });

  seller.forEach((sel, i) => {
    let s = sel; // 판매자
    let price = 100 * amount[i]; // 가격
    // 민호가 아닐 때까지 반복
    while (s !== "-") {
      const give = (price - (price % 10)) / 10; // 떼주는 돈
      money[s] += price - give; // 내가 갖는 돈
      price = give; // 떼준 돈으로 업데이트
      if (price === 0) break; // 0원이면 종료
      s = parents[s]; // 부모로 이동
    }
  });

  return enroll.map((e) => money[e]); // 각 판매원별 이익금의 총합
}
