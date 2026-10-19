def main():
    S = "#" + input()
    T = "#" + input()

    dp = [[0] * (len(T)) for _ in range(len(S))]

    # no need to initialize row0 and col0 with 0 since entire dp is 0-init

    for i in range(1, len(S)):
        for j in range(1, len(T)):
            if S[i] == T[j]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                a = dp[i-1][j]
                b = dp[i][j-1]
                dp[i][j] = max(a,b)
    
    print(dp[len(S)-1][len(T)-1])

if __name__ == '__main__':
    main()