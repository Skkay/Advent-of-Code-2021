with open('day-3/inputs.txt', 'r') as f:
    inputs = f.readlines()
    cols = len(inputs[0]) - 1 # skip \n

    gamma = ""
    epsilon = ""

    for i in range(0, cols):
        zero_occ =  0
        one_occ = 0
        for line in inputs:
            if line[i] == '0':
                zero_occ += 1
            else:
                one_occ += 1
        
        gamma += '0' if zero_occ > one_occ else '1'
        epsilon += '1' if zero_occ > one_occ else '0'
    
    print(int(gamma, 2) * int(epsilon, 2))
