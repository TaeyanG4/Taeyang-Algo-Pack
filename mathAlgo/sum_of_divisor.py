# divisor는 영어로 약수를 의미한다.
# gcd는 최대공약수를 의미한다. (greatest common divisor)
# lcm은 최소공배수를 의미한다. (least common multiple)

def sum_of_divisor1(n):
    """
        1부터 n까지의 약수의 합을 구하는 함수
    """
    return sum(k*(n//k) for k in range(1, n+1))

def sum_of_divisor2():
    """
        여러 1부터 n까지의 약수의 합을 구하는 함수
    """
    MX = 10**6
    memo = [0] * (MX+1)
    prefix_sum = [0] * (MX+1)
    for i in range(1, MX+1):
        j = 1
        while i*j <= MX:
            memo[i*j] += i
            j += 1
        prefix_sum[i] = prefix_sum[i-1] + memo[i]
    return prefix_sum


if __name__ == "__main__":
    
    # sum_of_divisor1
    n = int(input())
    print(sum_of_divisor1(n))
    
    # sum_of_divisor2
    prefix_sum = sum_of_divisor2()
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(prefix_sum[n])
        
    math.g