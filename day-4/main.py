def update_boards(boards, n):
    for i, board in enumerate(boards):
        for j, row in enumerate(board):
            for k, number in enumerate(row):
                if number == n:
                    number = '*'
                    boards[i][j][k] = '*'

        if check_win(board):
            return board

def check_win(board):
    for i, row in enumerate(board):
        if all('*' == number for number in row):
            return True
    
    for col in range(0, 5):
        if all('*' == row[col] for row in board):
            return True
    
    return False

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
    winning_board = None
    result = None
    for d in draw:
        winning_board = update_boards(boards, d)
        if winning_board:
            result = get_result(winning_board, int(d))
            break

    print(result)
