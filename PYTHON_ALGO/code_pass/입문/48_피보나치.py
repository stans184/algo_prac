def fibona(n):
    if n < 2:
        return n
    else:
        return fibona(n-1) + fibona(n-2)
    
# 시간이 엄청 걸림
# 40
# 102334155
# time :  12.946587085723877
    
def fibona2(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

# dynamic programming
# 40
# 102334155
# time :  4.961668252944946

def fibona3(n, memo={}):
    if n < 2:
        return n
    if n not in memo:
        memo[n] = fibona(n-1, memo) + fibona(n-2, memo)
    return memo[n]

import time
start_time = time.time()

print(fibona(int(input())))

print("time : ", time.time() - start_time)

start_time = time.time()

print(fibona2(int(input())))

print("time : ", time.time() - start_time)

start_time = time.time()

print(fibona3(int(input())))

print("time : ", time.time() - start_time)