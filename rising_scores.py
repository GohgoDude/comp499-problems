def displayMatrix(matrix):
    for line in matrix:
        print(line)

def main():
    length = int(input())
    scores = list(map(int, input().split()))

    scores.reverse()

    dp = [[0]*length for _ in range(length)]

    for i in range(length):
        dp[i][i] = 1

    largest = dp[0][0]

    for j in range(1, length):
        k = j-1
        for i in range(j-1, -1, -1):
            if scores[j] < scores[k]:
                a = dp[i+1][j]
                b = 1 + dp[0][k]
                dp[i][j] = max(a,b)
            else:
                dp[i][j] = dp[i+1][j]
            k -= 1
        if dp[0][j] > largest:
            largest = dp[0][j]

    displayMatrix(dp)
    print(largest)

if __name__ == '__main__':
    main()