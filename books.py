#import sys,io

#def test(s): sys.stdin=io.StringIO(s); main()

def main():
    n = int(input())
    books = list(map(int, input().split()))

    top = books[0]
    sum = books[0]
    for i in range(1, n):
        sum += books[i]
        if books[i] > top:
            top = books[i]
    print(max(2*top, sum))
    
# test("""3
# 2 8 3
# """)

# test("""3
# 2 3 4
# """)

# test("""1
# 5
# """)

if __name__ == '__main__':
    main()