import heapq

def main():
    # not doing anything with size. can maybe run bound checks
    size = int(input())
    inputs = list(map(int, input().split(" ")))
    heapq.heapify(inputs)

    min_cost = 0
    while len(inputs) > 1:
        a = heapq.heappop(inputs)
        b = heapq.heappop(inputs)
        c = a+b
        min_cost += c
        heapq.heappush(inputs, c)

    print(min_cost)
    
if __name__ == '__main__':
    main()