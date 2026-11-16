# import sys,io
# def test(s): sys.stdin=io.StringIO(s); main()

def decrement(clue, y_pos, x_pos):
    for y in range(y_pos-1, y_pos+2):
        for x in range(x_pos-1, x_pos+2):
            clue[y][x] -= 1
    return clue

def validation(clue, h, w):
    for y in range(0, h+2):
        for x in range(0, w+2):
            if clue[y][x] != 0:
                return False
    return True

def main():
    h, w = map(int, input().split())
    board = [['.'] * w for _ in range(h)]
    clue = [[0] * (w+2) for _ in range((h+2))]
    for j in range(h+2):
        clue[j] = list(map(int, input().split()))

    for y in range(1, h+1):
        for x in range(1, w+1):
            corner = clue[y-1][x-1]
            if corner > 0:
                clue = decrement(clue, y, x)
                # y-1 and x-1 is the associated position on the board with X and .
                board[y-1][x-1] = 'X'

    valid = validation(clue, h, w)

    if valid: 
        for line in board:
            print("".join(line))
    else:
        print("impossible")

# test("""2 3
# 1 1 2 1 1
# 1 2 3 2 1
# 1 2 3 2 1
# 0 1 1 1 0
# """)

# test("""1 2
# 0 0 1 1
# 0 1 1 1
# 0 1 1 1
# """)

if __name__ == '__main__':
    main()