import sys, io

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print(n)
    print(arr)


def test(s): sys.stdin=io.StringIO(s); main()

test("""4
4 3 2 6""")