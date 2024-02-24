def sieve_of_eratosthenes(n):
    sieve = [True] * (n + 1)  # 처음에는 모든 숫자를 소수로 가정
    sieve[0], sieve[1] = False, False  # 0과 1은 소수가 아니다

    for i in range(2, int(n**0.5) + 1):  # 2부터 n의 제곱근까지 검사
        if sieve[i]:  # i가 소수인 경우
            for j in range(i*i, n + 1, i):  # i의 제곱부터 시작하여 i의 배수들을 모두 지운다
                sieve[j] = False
    
    is_prime = [i for i in range(n + 1) if sieve[i]]
    return is_prime

# 주석 없는 버젼
def sieve_of_eratosthenes(n):
    sieve = [True] * (n + 1) 
    sieve[0], sieve[1] = False, False 

    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:  
            for j in range(i*i, n + 1, i):  
                sieve[j] = False
    
    is_prime = [i for i in range(n + 1) if sieve[i]]
    return is_prime


# 예시 사용 방법
n = 100
print(sieve_of_eratosthenes(n))  # 100 이하의 모든 소수를 출력