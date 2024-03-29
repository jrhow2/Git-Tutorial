from itertools import cycle
from helper_functions import (
    create_initial_game_board,
    show,
    make_move,
    determine_game_status
)


players = cycle(["X", "O"])
playing = True

while playing:

    # game preparations
    game_board = create_initial_game_board()
    game_status = determine_game_status(game_board)

    while game_status == "ongoing":
        show(game_board)

        # player move
        current_player = next(players)

        valid_move = False
        while not valid_move:
            try: 
                game_board = make_move(game_board, current_player)
                valid_move = True
                
            except Exception as e:
                print("\n")
                print("Something went wrong:", e)
                print("Hint: The chosen position must be available on the board.")
                print("Hint: The values must be separated by a comma e.g. '0, 1'.")
                print("Try again!", "\n")

        # stopping condition for while-loop
        game_status = determine_game_status(game_board)
        if game_status != "ongoing":
            show(game_board)
            print("Game finished!!!")

            if game_status == "draw":
                print("It is a draw! \n")
    else:
        print(f"Player {current_player} has achieved a {game_status}! \n")
            
    keep_playing = input("Do you want to play again? (y/n) ")
    if keep_playing != "y":
        playing = False