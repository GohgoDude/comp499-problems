import sys, io

def test(s): sys.stdin=io.StringIO(s); main()

def main():
    N,L = map(int, input().split())
    weights = list(map(int, input().split()))

    weights = sorted(weights)

    a = 0
    b = len(weights)-1

    boats = 0
    
    while a < b:
        if weights[a] + weights[b] <= L:
            a += 1
        b -= 1
        boats += 1
    if a == b:
        boats += 1
    print(boats)

test("""4 7
1 5 3 5""")

test("""4 6
1 2 4 5""")

# if __name__ == '__main__':
#     main()