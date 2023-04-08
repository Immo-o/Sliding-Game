from helpers.board_helpers import get_random_board, display_board, to_one_dimension


def main():
    board = get_random_board(N=5)
    display_board(to_one_dimension(board))


if __name__ == "__main__":
    main()
