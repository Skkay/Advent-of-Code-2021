with open('day-3/inputs.txt', 'r') as f:
    inputs = f.readlines()
    cols = len(inputs[0]) - 1 # skip \n

    oxygen_generator = inputs.copy()
    co2_scrubber = inputs.copy()

    for i in range(0, cols):
        zero_occ =  0
        one_occ = 0

        for line in oxygen_generator:
            if line[i] == '0':
                zero_occ += 1
            else:
                one_occ += 1
        
        if zero_occ > one_occ:
            for line in oxygen_generator.copy():
                if len(oxygen_generator) > 1 and line[i] == '1':
                    oxygen_generator.remove(line)
        else:
            for line in oxygen_generator.copy():
                if len(oxygen_generator) > 1 and line[i] == '0':
                    oxygen_generator.remove(line)

        zero_occ =  0
        one_occ = 0
        for line in co2_scrubber:
            if line[i] == '0':
                zero_occ += 1
            else:
                one_occ += 1
        
        if zero_occ > one_occ:
            for line in co2_scrubber.copy():
                if len(co2_scrubber) > 1 and line[i] == '0':
                    co2_scrubber.remove(line)
        else:
            for line in co2_scrubber.copy():
                if len(co2_scrubber) > 1 and line[i] == '1':
                    co2_scrubber.remove(line)
        

    print(int(oxygen_generator[0], 2) * int(co2_scrubber[0], 2))
