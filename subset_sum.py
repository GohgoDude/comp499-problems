#import math

def main():
    #size, target = map(int, input().split())
    #numbers = list(map(int, input().split()))
    size, target = 6, 9
    numbers = [3, 34, 4, 12, 5, 2]

    # b_integers = [0]*len(integers)

    # for i in range(1, math.pow(2, len(integers))):
    #     binary_num = 

    start = 0 # allows us to determine where to start without excess backtracking
    i = 0
    total = 0
    skip = set()
    while start < size:    
        # if start is increased, reset skip = set()
        if total < target:
            total += numbers[i]
            i += 1
        elif total > target:
            total -= numbers[i-1]
            # i stays in place
        # if I reach the end of the array and I am above T still, then start+=1 and skip = set() (reset)
    
    def subset_sum(numbers, target, index=0, current_sum=0):
        if current_sum == target:
            return True
        


if __name__ == '__main__':
    main()