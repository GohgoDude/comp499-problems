#import sys,io

#def test(s): sys.stdin=io.StringIO(s); main()

def main():
    n = int(input())
    nums = list(map(int, input().split()))

    myset = set()
    count = 0

    for i in range(n):
        if nums[i]-1 not in myset:
            count += 1
        myset.add(nums[i])
    print(count)

# test("""5
# 4 2 1 5 3
# """)

# test("""4
# 1 2 3 4
# """)

# test("""3
# 3 2 1
# """)

if __name__ == '__main__':
    main()