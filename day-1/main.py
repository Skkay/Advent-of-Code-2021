with open('day-1/inputs.txt', 'r') as f:
    inputs = f.readlines()

    last = int(inputs[0])
    inputs.pop(0)

    count = 0
    for line in inputs:
        if int(line) > last:
            count += 1

        last = int(line)

    print(count)
