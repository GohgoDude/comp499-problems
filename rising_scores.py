def main():
    N = int(input())
    scores = list(map(int, input().split()))

    scores.reverse()

    dp = [[0]*N for _ in range(N)]

    for i in range(N):
        dp[i][i] = 1

    largest = dp[0][0]

    solutions = [[] for _ in range(N)]
    solutions[0] = [N-1]

    # for solution in solutions:
    #     print(solution)
    #     print(len(solutions))

    sub_solutions = []

    for j in range(1, N):
        sub_solutions.clear()
        sub_solutions.append([N-1-j])
        k = j-1
        for i in range(j-1, -1, -1):
            if scores[j] < scores[k]:
                a = dp[i+1][j]
                b = 1 + dp[0][k]
                dp[i][j] = max(a,b)
                # wip
            else:
                dp[i][j] = dp[i+1][j]
            k -= 1
        if dp[0][j] > largest:
            largest = dp[0][j]

    # for line in dp:
    #     print(line)
    print(largest)

if __name__ == '__main__':
    main()