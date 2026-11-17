import sys,io

def test(s): sys.stdin=io.StringIO(s); main()

def find_closest(arr, target):
    if target <= arr[0]:
        return 0
    if target >= arr[-1]:
        return len(arr)-1

    left, right = 0, len(arr)-1

    while left <= right:
        mid = left + (right-left)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid+1
        else:
            right = mid+1
    
    if abs(arr[right] - target) <= abs(arr[left] - target):
        return right
    else:
        return left

def main():
    n = int(input())
    books = list(map(int, input().split()))

    books = sorted(books)

    cost = 0

    A = []
    B = []
    A_val = 0
    B_val = 0

    while books:
        A.append(books.pop())
        A_val = A[0]
        while books and (B_val+books[-1] <= A_val):
            B.append(books.pop())
            B_val += B[-1]
        if A_val != B_val and books:
            target = A_val-B_val
            closest = find_closest(books, target)
            B.append(books.pop(closest))
            B_val += B[-1]

        if not books or target == closest:
            cost += 2 * max(A_val, B_val)
        
        B_val = 0
    print(cost)

test("""3
2 8 3
""")

test("""3
2 3 4
""")

test("""1
5
""")

# if __name__ == '__main__':
#     main()