with open('day-1/inputs.txt', 'r') as f:
    inputs = f.readlines()

    last = int(inputs[0]) + int(inputs[1]) + int(inputs[2])

    count = 0
    for index, line in enumerate(inputs):
        try:
            current = int(inputs[index]) + int(inputs[index + 1]) + int(inputs[index + 2])

            if current > last:
                count += 1
            
            last = current
        except IndexError:
            print("Not enough data")

    print(count)
