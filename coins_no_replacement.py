def main():
    N,M = map(int, input().split())
    coins = list(map(int, input().split()))

    coins = [0] + coins

    dp = [[0] * (N+1) for _ in range(M+1)]

    # not needed because entire dp table is already 0-set
    # also this code might be wrong lol
    # for i in range(N+1):
    #     dp[i][0] = 0

    # impossible solution prefill
    for j in range(1, M+1):
        dp[j][0] = -1
        
    for i in range(1, N+1):
        for j in range(1, M+1):
            if j - coins[i] == 0:
                dp[j][i] = 1
            elif j - coins[i] < 0:
                dp[j][i] = dp[j][i-1]
            else:
                a = 1 + dp[j-coins[i]][i-1]
                b = dp[j][i-1]
                if b < 0 and a <= 0:
                    dp[j][i] = -1
                elif b < 0 and a > 0:
                    dp[j][i] = a
                elif b > 0 and a <= 0:
                    dp[j][i] = b
                else:
                    dp[j][i] = min(a,b)
    
    print(dp[M][N])
    
if __name__ == '__main__':
    main()