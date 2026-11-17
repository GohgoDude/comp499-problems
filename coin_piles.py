# import sys,io

# def test(s): sys.stdin=io.StringIO(s); main()

def main():
    n = int(input())
    for _ in range(n):
        a, b = map(float, input().split())
        temp = a
        if a < b:
            a = b
            b = temp
        if (a+b) % 3 == 0 and (a-b) <= (a/2):
            print("YES")
        else:
            print("NO")
    print()

# test("""1
# 4 5
# """)

# test("""3
# 2 1
# 2 2
# 3 3
# """)

# test("""5
# 0 0
# 0 3
# 1 2
# 1 1
# 2 4
# """)

# test("""3
# 1000000000 500000000
# 1000000000 1000000000
# 999999999 999999999
# """)

if __name__ == '__main__':
    main()