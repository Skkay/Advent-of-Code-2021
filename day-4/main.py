def update_boards(boards, n):
    for i, board in enumerate(boards):
        for j, row in enumerate(board):
            for k, number in enumerate(row):
                if number == n:
                    number = '*'
                    boards[i][j][k] = '*'

def check_win(boards):
    for board in boards:
        for row in board:
            if all('*' == number for number in row):
                try:
                    boards.remove(board)
                except ValueError:
                    pass
        for col in range(0, len(row)):
            if all('*' == row[col] for row in board):
                try:
                    boards.remove(board)
                except ValueError:
                    pass

def get_result(winning_board, d):
    a = 0
    for row in winning_board:
        a += sum(int(number) for number in row if number != '*')

    return a * d


with open('day-4/inputs.txt', 'r') as f:
    inputs = f.readlines()

    draw = inputs[0][:-1].split(',')
    del inputs[0]

    # boards construction
    boards = []
    for line in inputs:
        if line == '\n': # new board
            board = []
            boards.append(board)
            continue

        row = [(line[i:i+3]).strip() for i in range(0, len(line), 3)]
        board.append(row)
    
    # draw
    for d in draw:
        update_boards(boards, d)
        if (len(boards)) == 1:
            result = get_result(boards[0], int(d))
        check_win(boards)

        if len(boards) == 0:
            print(result)
            break
