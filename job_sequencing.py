def main():
    size = int(input())
    inputs = []
    slots = [-1]*size
    total = 0

    for _ in range(size):
        a,b = input().split(" ")
        inputs.append((int(a), int(b)))

    sorted_inputs = sorted(inputs, key=lambda x: x[1], reverse=True)

    #print(sorted_inputs)

    for i in range(size):
        probe = sorted_inputs[i][0] - 1
        while probe >= 0 and slots[probe] != -1:
            probe -= 1
        if probe > -1:
            slots[probe] = sorted_inputs[i][1]
            total += sorted_inputs[i][1]
    #print(slots)
    print(total)

if __name__ == '__main__':
    main()