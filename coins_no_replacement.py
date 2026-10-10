def main():
    C,M = map(int, input().split())
    integers = list(map(int, input().split()))

    dp = [[0] * (C+1) for _ in range(M)]

    print(dp)

    for j in range(C):
        for i in range(M+1):
            
    
if __name__ == '__main__':
    main()