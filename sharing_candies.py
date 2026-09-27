import heapq

def main():
    N,M = map(int, input().split(" "))
    
    greed_factors = list(map(int, input().split()))
    candy_sizes = list(map(int, input().split()))
    greed_factors = [-x for x in greed_factors]
    candy_sizes = [-x for x in candy_sizes]

    heapq.heapify(greed_factors)
    heapq.heapify(candy_sizes)

    happy_kids = 0

    while greed_factors and candy_sizes:
        if candy_sizes[0]*-1 >= greed_factors[0]*-1:
            happy_kids += 1
            heapq.heappop(candy_sizes)
            heapq.heappop(greed_factors)
        else:
            heapq.heappop(greed_factors)

    print(happy_kids)

if __name__ == '__main__':
    main()