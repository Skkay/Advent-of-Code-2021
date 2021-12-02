with open('day-2/inputs.txt', 'r') as f:
    inputs = f.readlines()
    
    total = { 'h_position': 0, 'depth': 0, 'aim': 0 }
    for line in inputs:
        dir, value = line.split(' ')

        if dir == 'forward':
            total['h_position'] += int(value)
            total['depth'] += total['aim'] * int(value)
        elif dir == 'down':
            total['aim'] += int(value)
        elif dir == 'up':
            total['aim'] -= int(value)
    
    print(total['h_position'] * total['depth'])
