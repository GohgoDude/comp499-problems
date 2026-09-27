def main():

    size = int(input())
    inputs = []

    for _ in range(size):
        a, b = input().split(" ")
        inputs.append((int(a), int(b)))
    
    sorted_inputs = sorted(inputs, key=lambda x: x[1])

    #print(sorted_inputs)
    pointer = sorted_inputs[0][0]
    paths_taken = 0
    for i in range(size):
        if pointer > sorted_inputs[i][0]:
            continue
        paths_taken += 1
        pointer = sorted_inputs[i][1]
    print(paths_taken)
if __name__ == '__main__':
   main()