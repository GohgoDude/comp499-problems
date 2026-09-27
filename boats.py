def main():
    N,L = map(int, input().split())
    weights = list(map(int, input().split()))

    weights = sorted(weights)

    a = 0
    b = len(weights)-1

    boats = 0

    if len(weights) == 1:
        boats += 1

    while a < b:
        if weights[a] + weights[b] == L:
            boats += 1
            a += 1
            b -= 1
            #print("execute A)")
        elif weights[a] + weights[b] < L:
            if a+1 != b:
                boats += 1
            a += 1
            #print("execute B")
        else:
            #cant do if a != b-1 because current a,b are necessarily
            # over L so they cannot be together
            boats += 1
            b -= 1
            #print("execute C")
        if a == b:
            boats += 1
            #print("execute D")
    print(boats)

if __name__ == '__main__':
    main()