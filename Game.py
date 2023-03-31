from helpers.board_helpers import get_random_board, display_board


def main():
    board = get_random_board(N=3)
    display_board(board)


if __name__ == "__main__":
    main()
