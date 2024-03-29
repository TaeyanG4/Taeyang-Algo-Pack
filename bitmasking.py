# https://travelbeeee.tistory.com/451 비트마스킹 이란?
# https://zzonglove.tistory.com/43

# bm | (1 << i) : i번째 비트 활성화 하기
# bm & !(1 << i) : i번째 비트 비활성화 하기
# bm & (1 << i) : i번째 비트가 활성화 되어있는지 확인하기
# bm & (bm - 1) : 가장 오른쪽에 있는 비트를 하나만 끄기
# bm & -bm : 가장 오른쪽에 있는 비트를 하나만 켜기
# bm & (bm + 1) : 가장 오른쪽에 있는 0을 하나만 켜기
# bm & !(bm + 1) : 가장 오른쪽에 있는 1을 하나만 끄기
# bm & (bm - 1) : 가장 오른쪽에 있는 1을 하나만 끄기