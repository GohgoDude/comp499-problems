import sys,io

def test(s): sys.stdin=io.StringIO(s); main()

def main():
    n = int(input())
    books = list(map(int, input().split()))

    books = sorted(books)

    book_list = []
    for i in range(len(books)):
        book_list.append((books[i], i))
    
    print(book_list)

    cost = 0

    A = []
    B = []
    A_val = 0
    B_val = 0

    
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