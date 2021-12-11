with open('day-9/inputs.txt', 'r') as f:
    inputs = f.readlines()

map = []
for line in inputs:
    row = [int(cell) for cell in list(line.strip())]
    map.append(row)

risk_sum = 0
for y, row in enumerate(map):
    for x, cell in enumerate(row):
        n_right = row[x + 1] if x + 1 < len(row) else 9
        n_left = row[x - 1] if x - 1 > -1 else 9
        n_top = map[y + 1][x] if y + 1 < len(map) else 9
        n_bottom = map[y - 1][x] if y - 1 > -1 else 9

        if cell < n_right and cell < n_left and cell < n_top and cell < n_bottom:
            risk_sum += cell + 1

print(risk_sum)
