from function import print_board, generate_piece

def main(game_board: [[int, ], ]) -> [[int, ], ]:
    # Seed the board with two tiles to start with
    piece1 = generate_piece(game_board)
    game_board[piece1['row']][piece1['column']] = piece1['value']
    
    piece2 = generate_piece(game_board)
    while (piece2['row'], piece2['column']) == (piece1['row'], piece1['column']):
        piece2 = generate_piece(game_board)  # make sure the two starting tiles are different
    game_board[piece2['row']][piece2['column']] = piece2['value']

    print_board(game_board)


    while not game_over(game_board):
        turn = input("Enter your move (w/a/s/d or q to quit): ").lower()
        while turn not in ['w', 'a', 's', 'd', 'q']:
            print('You entered an invalid input. Please try again.')
            turn = input().lower()

        if turn == 'q':
            print("Goodbye!")
            break

        board_changed = False
        if turn == 'a':
            board_changed = move_left(game_board)
        elif turn == 'd':
            board_changed = move_right(game_board)
        elif turn == 'w':
            board_changed = move_up(game_board)
        elif turn == 's':
            board_changed = move_down(game_board)

        if board_changed:  # Add a new piece only if board has changed
            piece = generate_piece(game_board)
            game_board[piece['row']][piece['column']] = piece['value']
            print_board(game_board)

    print("Game Over!")
    print_board(game_board)

def move_left(board):
    board_changed = False
    for row in board:
        # 1. Shift
        non_zero_tiles = [tile for tile in row if tile != 0]
        while len(non_zero_tiles) < 4:
            non_zero_tiles.append(0)
        # 2. Merge
        i = 0
        while i < 3:
            if non_zero_tiles[i] == non_zero_tiles[i + 1] and non_zero_tiles[i] != 0:
                non_zero_tiles[i] *= 2
                non_zero_tiles[i + 1] = 0
                i += 2
                board_changed = True
            else:
                i += 1
        # 3. Shift again after merging
        new_row = [tile for tile in non_zero_tiles if tile != 0]
        while len(new_row) < 4:
            new_row.append(0)
        # Check if row has changed
        if row != new_row:
            board_changed = True
            for i in range(4):
                row[i] = new_row[i]
    return board_changed

def move_right(board):
    board_changed = False
    for row in board:
        # 1. Shift
        non_zero_tiles = [tile for tile in row if tile != 0]
        while len(non_zero_tiles) < 4:
            non_zero_tiles.insert(0, 0)
        # 2. Merge
        i = 3
        while i > 0:
            if non_zero_tiles[i] == non_zero_tiles[i - 1] and non_zero_tiles[i] != 0:
                non_zero_tiles[i] *= 2
                non_zero_tiles[i - 1] = 0
                i -= 2
                board_changed = True
            else:
                i -= 1
        # 3. Shift again after merging
        new_row = [tile for tile in non_zero_tiles if tile != 0]
        while len(new_row) < 4:
            new_row.insert(0, 0)
        # Check if row has changed
        if row != new_row:
            board_changed = True
            for i in range(4):
                row[i] = new_row[i]
    return board_changed

def move_up(board):
    board_changed = False
    for col in range(4):
        # 1. Shift
        non_zero_tiles = [board[row][col] for row in range(4) if board[row][col] != 0]
        while len(non_zero_tiles) < 4:
            non_zero_tiles.append(0)
        # 2. Merge
        i = 0
        while i < 3:
            if non_zero_tiles[i] == non_zero_tiles[i + 1] and non_zero_tiles[i] != 0:
                non_zero_tiles[i] *= 2
                non_zero_tiles[i + 1] = 0
                i += 2
                board_changed = True
            else:
                i += 1
        # 3. Shift again after merging
        new_col = [tile for tile in non_zero_tiles if tile != 0]
        while len(new_col) < 4:
            new_col.append(0)
        # Check if col has changed
        for row in range(4):
            if board[row][col] != new_col[row]:
                board_changed = True
                board[row][col] = new_col[row]
    return board_changed

def move_down(board):
    board_changed = False
    for col in range(4):
        # 1. Shift
        non_zero_tiles = [board[row][col] for row in range(4) if board[row][col] != 0]
        while len(non_zero_tiles) < 4:
            non_zero_tiles.insert(0, 0)
        # 2. Merge
        i = 3
        while i > 0:
            if non_zero_tiles[i] == non_zero_tiles[i - 1] and non_zero_tiles[i] != 0:
                non_zero_tiles[i] *= 2
                non_zero_tiles[i - 1] = 0
                i -= 2
                board_changed = True
            else:
                i -= 1
        # 3. Shift again after merging
        new_col = [tile for tile in non_zero_tiles if tile != 0]
        while len(new_col) < 4:
            new_col.insert(0, 0)
        # Check if col has changed
        for row in range(4):
            if board[row][col] != new_col[row]:
                board_changed = True
                board[row][col] = new_col[row]
    return board_changed

def game_over(game_board: [[int, ], ]) -> bool:
    for i in range(4):
        for j in range(4):
            if game_board[i][j] == 0:  # Check if there's an empty spot
                return False
            if i < 3 and game_board[i][j] == game_board[i + 1][j]:  # Check vertical merges
                return False
            if j < 3 and game_board[i][j] == game_board[i][j + 1]:  # Check horizontal merges
                return False
    return True

if __name__ == "__main__":
    main([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]])
