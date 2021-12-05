def update_map(map, x_pos, y_pos):
    for x in range(min(x_pos), max(x_pos) + 1):
        for y in range(min(y_pos), max(y_pos) + 1):
            map[x][y] += 1

def get_result(map):
    count = 0
    for row in map:
        for cell in row:
            if cell > 1:
                count += 1

    return count


with open('day-5/inputs.txt', 'r') as f:
    inputs = f.readlines()

    max_x = 0
    max_y = 0
    lines = []
    for input in inputs:
        from_pos, to_pos = input.split(' -> ')
        line = {
            'x1': int(from_pos.split(',')[0]),
            'y1': int(from_pos.split(',')[1]),
            'x2': int(to_pos.split(',')[0]),
            'y2': int(to_pos.split(',')[1]),
        }
        lines.append(line)

        # get the max x and max y
        if line['x1'] > max_x:
            max_x = line['x1']
        if line['x2'] > max_x:
            max_x = line['x2']
        if line['y1'] > max_y:
            max_y = line['y1']
        if line['y2'] > max_y:
            max_y = line['y2']


map = [[0 for _ in range(0, max_y + 1)] for _ in range(0, max_x + 1)]
for line in lines:
    if line['x1'] == line['x2'] or line['y1'] == line['y2']: # part 1: only horizontal or vertical lines
        update_map(map, (line['x1'], line['x2']), (line['y1'], line['y2']))


print(get_result(map))
