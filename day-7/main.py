with open('day-7/inputs.txt', 'r') as f:
    inputs = f.readlines()

positions = [int(x) for x in inputs[0].split(',')]
positions.sort()
median = positions[len(positions)//2]

needed_fuel = sum(abs(median - pos) for pos in positions)
print(needed_fuel)
