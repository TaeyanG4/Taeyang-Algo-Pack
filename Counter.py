from collections import Counter

lst = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9, 9]
count = Counter(lst)

for item, freq in count.items():
    print(f"{item}는 {freq}개 있습니다.")

print(count)
print(count.most_common(2)) # 가장 빈도가 높은 2개의 아이템을 출력합니다.