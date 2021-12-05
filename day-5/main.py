def update_map(map, x_pos, y_pos):
    # horizontal or vertical lines
    if x_pos[0] == x_pos[1] or y_pos[0] == y_pos[1]: 
        for x in range(min(x_pos), max(x_pos) + 1):
            for y in range(min(y_pos), max(y_pos) + 1):
                map[x][y] += 1
    
    # diagonal lines
    else:
        # reverse direction
        if x_pos[0] > x_pos[1]:
            x_pos[0], x_pos[1] = x_pos[1], x_pos[0]
            y_pos[0], y_pos[1] = y_pos[1], y_pos[0]

        diff = x_pos[1] - x_pos[0]

        # diagonal from top left to bottom right and bottom right to top left
        if (x_pos[0] < x_pos[1] and y_pos[0] < y_pos[1]) or (x_pos[0] > x_pos[1] and y_pos[0] > y_pos[1]):
            for i in range(0, diff + 1):
                map[x_pos[0] + i][y_pos[0] + i] += 1
        
        # diagonal from top right to bottom left and bottom left to top right
        elif (x_pos[0] > x_pos[1] and y_pos[0] < y_pos[1]) or (x_pos[0] < x_pos[1] and y_pos[0] > y_pos[1]):
            for i in range(0, diff + 1):
                map[x_pos[0] + i][y_pos[0] - i] += 1

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
    update_map(map, [line['x1'], line['x2']], [line['y1'], line['y2']])


print(get_result(map))
