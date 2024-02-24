# gpt4
import math

class SparseTable:
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)
        self.logn = int(math.log2(self.n)) + 1
        self.st = [[0] * (self.logn + 1) for _ in range(self.n)]
        
        # 초기화
        for i in range(self.n):
            self.st[i][0] = i
        
        # 구간의 길이를 2의 승수로 늘려가며 테이블 채우기
        for j in range(1, self.logn + 1):
            i = 0
            while i + (1 << j) <= self.n:
                # i 부터 시작하는 길이 2^j 구간의 최소값을 저장
                if arr[self.st[i][j-1]] < arr[self.st[i + (1 << (j-1))][j-1]]:
                    self.st[i][j] = self.st[i][j-1]
                else:
                    self.st[i][j] = self.st[i + (1 << (j-1))][j-1]
                i += 1
                
        print(self.st)
                
    def query(self, l, r):
        """ l과 r 사이의 최소값을 반환 """
        length = r - l + 1
        k = int(math.log2(length))
        
        if self.arr[self.st[l][k]] <= self.arr[self.st[r - (1 << k) + 1][k]]:
            return self.arr[self.st[l][k]]
        else:
            return self.arr[self.st[r - (1 << k) + 1][k]]

if __name__ == "__main__":
    
    # 예제 사용
    arr = [2, 4, 3, 1, 6, 7, 8, 9, 1, 7]
    st = SparseTable(arr)
    print(st.query(0, 3))  # 1
    print(st.query(4, 9))  # 1
    print(st.query(3, 6))  # 1