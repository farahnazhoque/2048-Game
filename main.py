
from function import generate_piece, print_board

DEV_MODE = True


def main(game_board: [[int, ], ]) -> [[int, ], ]:
    """
    2048 main function, runs a game of 2048 in the console.

    Uses the following keys:
    w - shift up
    a - shift left
    s - shift down
    d - shift right
    q - ends the game and returns control of the console
    :param game_board: a 4x4 2D list of integers representing a game of 2048
    :return: returns the ending game board
    """
    # Initialize board's first cell

    # TODO: generate a random piece and location using the generate_piece function
    # TODO: place the piece at the specified location
    our_dict = generate_piece(game_board)
    '''game_board[our_dict['row']][our_dict['column']] = our_dict['value']'''
    '''game_board[0][1] = 4
    game_board[0][2] = 4
    game_board[1][0] = 64
    game_board[2][0] = 64
    game_board[3][1] = 128
    game_board[3][2] = 128
    game_board[3][3] = 0'''

    print(print_board(game_board))

    # Initialize game state trackers
    '''how to stop replacing 2 with other occupied indexes'''
    '''why is 's' not working'''
    '''starting the game over function'''
    '''is my code successive?'''

    # Game Loop
    while True:

        # TODO: Reset user input variable

        # TODO: Take computer's turn
        # place a random piece on the board
        # check to see if the game is over using the game_over function

        # TODO: Show updated board using the print_board function

        # TODO: Take user's turn
        # Take input until the user's move is a valid key
        # if the user quits the game, print Goodbye and stop the Game Loop
        # Execute the user's move

        # Check if the user wins
        player = 0
        while player == 0:
            player += 1
            turn = input()
            if turn.lower() != 'w' and turn.lower() != 'a' and turn.lower() != 's' and turn.lower() != 'd' and turn.lower() != 'q':
                print('You entered an invalid input. Please try again.')

            if turn.lower() == 'a':
                shift_completed = False
                merge = False
                while not shift_completed:
                    for i in range(4):
                        z = 0
                        for j in range(4):
                            if game_board[i][j] != 0:
                                game_board[i][z] = game_board[i][j]
                                if z != j:
                                    game_board[i][j] = 0

                                z += 1
                    if merge:
                        shift_completed = True
                    if not merge:
                        for i in range(4):
                            for j in range(4):
                                if 0 < j:
                                    if game_board[i][j] == game_board[i][j - 1]:
                                        game_board[i][j - 1] = game_board[i][j - 1] * 2
                                        game_board[i][j] = 0
                                        merge = True
            elif turn.lower() == 'd':
                shift_completed = False
                merge = False
                while not shift_completed:
                    for i in range(4):
                        z = 3
                        for j in range(3, -1, -1):
                            if game_board[i][j] != 0:
                                game_board[i][z] = game_board[i][j]
                                if z != j:
                                    game_board[i][j] = 0

                                z -= 1
                    if merge:
                        shift_completed = True
                    if not merge:
                        for i in range(4):
                            for j in range(4):
                                if 0 < j:
                                    if game_board[i][j] == game_board[i][j - 1]:
                                        game_board[i][j - 1] = game_board[i][j - 1] * 2
                                        game_board[i][j] = 0
                                        merge = True

            elif turn.lower() == 's':
                shift_completed = False
                merge = False
                while not merge:
                    for i in range(2, -1, -1):
                        for j in range(4):
                            if game_board[i + 1][j] == game_board[i][j]:
                                game_board[i + 1][j] = game_board[i + 1][j] * 2
                                game_board[i][j] = 0
                            if game_board[2][j] == game_board[1][j]:
                                game_board[2][j] *= 2
                                game_board[1][j] = 0
                            if game_board[3][j] == game_board[2][j]:
                                game_board[3][j] *= 2
                                game_board[2][j] = 0

                            if shift_completed:
                                merge = True
                            elif not shift_completed:
                                for j in range(4):
                                    for i in range(3):
                                        if game_board[i][j] != 0:
                                            if game_board[i + 1][j] == 0:
                                                game_board[i + 1][j] = game_board[i][j]
                                                game_board[i][j] = 0
                                                shift_completed = True
            elif turn.lower() == 'w':
                shift_completed = False
                merge = False
                while not shift_completed:
                    for i in range(3):
                        for j in range(4):
                            if game_board[i - 1][j] == 0 and game_board[i][j] != 0:
                                game_board[i - 1][j] = game_board[i][j]
                                if i - 1 != i:
                                    game_board[i][j] = 0

                    if merge:
                        shift_completed = True
                    if not merge:
                        for i in range(3):
                            for j in range(4):
                                if game_board[i][j] == game_board[i - 1][j]:
                                    game_board[i - 1][j] = game_board[i - 1][j] * 2
                                    game_board[i][j] = 0
                                    merge = True
            game_board[our_dict['row']][our_dict['column']] = our_dict[
                'value']  # we are assigning True so that this does not run again
        print(print_board(game_board))

        break

    return game_board


def game_over(game_board: [[int, ], ]) -> bool:
    """
    Query the provided board's game state.

    :param game_board: a 4x4 2D list of integers representing a game of 2048
    :return: Boolean indicating if the game is over (True) or not (False)
    """
    # TODO: Loop over the board and determine if the game is over
    return False  # TODO: Don't always return false


if __name__ == "__main__":
    main([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]])


