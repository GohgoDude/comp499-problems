def main():
    lines = int(input())
    inputs = []
    for _ in range(lines):
        y,x = input().split(" ")
        inputs.append((int(y), int(x)))

    for i in range(lines):
        y,x = inputs[i]
        k = max(y,x)
        diag_val = k*k - (k-1)

        # need to also check odd or even
        if k == x:
            if k % 2 == 1:
                val = diag_val + (k - y)
            else:
                val = diag_val - (k - y)
        else:
            if k % 2 == 1:
                val = diag_val - (k - x)
            else:
                val = diag_val + (k - x)
        print(val)

if __name__ == '__main__':
    main()