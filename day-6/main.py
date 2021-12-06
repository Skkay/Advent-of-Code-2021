with open('day-6/inputs.txt', 'r') as f:
    inputs = f.readlines()

    initial_state = [int(x) for x in inputs[0].split(',')]

    for day in range(80):
        for index in range(len(initial_state)):
            if initial_state[index] == 0:
                initial_state[index] = 7
                initial_state.append(8)

            initial_state[index] -= 1

print(len(initial_state))
