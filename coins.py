import heapq

def main():
    N,M = map(int, input().split())
    coins = list(map(int, input().split()))

    dp = [0] * (M+1)

    for i in range(1, M+1):
        best = None
        for coin in coins:
            if coin <= i and dp[i-coin] >= 0:
                candidate = 1 + dp[i-coin]
                if best is None or candidate < best:
                    best = candidate
        if best is None:
            dp[i] = -1
        else:
            dp[i] = best

    print(dp[-1])
    
if __name__ == '__main__':
    main()