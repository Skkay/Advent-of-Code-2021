with open('day-7/inputs.txt', 'r') as f:
    inputs = f.readlines()

positions = [int(x) for x in inputs[0].split(',')]
positions.sort()

mean = sum(pos for pos in positions) // len(positions)

needed_fuel = sum((abs(mean - pos)**2 + abs(mean - pos)) // 2 for pos in positions)
print(needed_fuel)
