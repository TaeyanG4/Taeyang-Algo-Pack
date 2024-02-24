"""
    시간 복잡도: 두 알고리즘 모두 패턴에 대한 실패 함수(lps 또는 skip)를 계산하는 데 O(m)의 시간이 걸리며, 
        텍스트에서 패턴을 검색하는 데도 O(n)의 시간이 걸립니다. 따라서 두 알고리즘 모두 시간 복잡도는 O(n + m)이다.
    
    공간 복잡도: 두 알고리즘 모두 패턴의 길이에 비례하는 추가 공간을 사용합니다. 따라서 공간 복잡도는 O(m)이다.
    
    # 모든 일치하는 위치를 찾아야 한다면 kmp_search1()을 사용하는 것이 적합하다.
    # 첫 번째 일치하는 위치만 필요한 경우 kmp_search2()을 사용하는 것이 적합하다.
    # 패턴의 발생 횟수와 위치 모두 알고 싶다면 kmp_search3()을 사용하는것이 적합하다.
    
    LPS는 'Longest Proper Prefix which is also Suffix'의 약자이다.
"""

############################################################################################
############################################################################################

# KMP(Knuth-Morris-Pratt) Algorithm
# GPT-4
def compute_lps1(pattern):
    length = 0  # 이전의 lps 값을 기억

    lps = [0] * len(pattern)  # lps 초기화
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_search1(text, pattern):
    # 실패 함수 생성
    lps = compute_lps1(pattern)
    
    i = 0  # text의 현재 위치
    j = 0  # pattern의 현재 위치
    
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == len(pattern):
            print("Pattern found at index " + str(i - j))
            j = lps[j - 1]

        # mismatch 후 j!=0인 경우
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

############################################################################################
############################################################################################
# [Do it! 실습 7-2] KMP법으로 문자열 검색하기
def kmp_search2(txt: str, pat: str) -> int:
    """KMP법에 의한 문자열 검색"""
    pt = 1  # txt를 따라가는 커서
    pp = 0  # pat를 따라가는 커서
    skip = [0] * (len(pat) + 1)  # 건너뛰기 표

    # 건너뛰기 표 만들기 compute_lps()와 동일
    skip[pt] = 0
    while pt != len(pat):
        if pat[pt] == pat[pp]:
            pt += 1
            pp += 1
            skip[pt] = pp
        elif pp == 0:
            pt += 1
            skip[pt] = pp
        else:
            pp = skip[pp]

    # 검색하기
    pt = pp = 0
    while pt != len(txt) and pp != len(pat):
        if txt[pt] == pat[pp]:
            pt += 1
            pp += 1
        elif pp == 0:
            pt += 1
        else:
            pp = skip[pp]

    return pt - pp if pp == len(pat) else -1

def compute_lps2(pat: str) -> int:
    pt = 1 
    pp = 0  
    skip = [0] * (len(pat) + 1)  

    skip[pt] = 0
    while pt != len(pat):
        if pat[pt] == pat[pp]:
            pt += 1
            pp += 1
            skip[pt] = pp
        elif pp == 0:
            pt += 1
            skip[pt] = pp
        else:
            pp = skip[pp]
    
    return skip

############################################################################################
############################################################################################
# https://hooongs.tistory.com/305
def compute_lps3(p):
    pi = [0 for _ in range(len(p))]
    
    j = 0
    for i in range(1, len(p)):
        while j > 0 and p[i] != p[j]:
            j = pi[j-1]
            
        if p[i] == p[j]:
            j += 1
            pi[i] = j
            
    return pi
        
def kmp_search3(t, pi):
    cnt = 0
    pos = []
    
    j = 0
    for i in range(len(t)):
        while j > 0 and t[i] != pattern[j]:
            j = pi[j-1]
            
        if t[i] == pattern[j]:
            if j == len(pattern)-1:
                cnt += 1
                pos.append(i-len(pattern)+2)
                j = pi[j]
            else:
                j += 1
    return cnt, pos

############################################################################################
############################################################################################
# for test
if __name__ == '__main__':
    
    text = "ABABDABACDABABCABAB"# 텍스트용 문자열
    pattern = "ABABCABAB"    # 패턴용 문자열
    
    ########################################################################
    # GPT-4
    # 사용 예제
    kmp_search1(text, pattern)
    
    ########################################################################
    # [Do it! 실습 7-2] KMP법으로 문자열 검색하기
    idx = kmp_search2(text, pattern)  # 문자열 s1~s2를 KMP법으로 검색
    if idx == -1:
        print('텍스트 안에 패턴이 존재하지 않습니다.')
    else:
        print(f'{(idx + 1)}번째 문자에서 일치합니다.')
    
    ########################################################################
    # https://hooongs.tistory.com/305
    cnt, pos = kmp_search3(text, compute_lps3(pattern))
    print(cnt)
    print(*pos)