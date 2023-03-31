import random


def get_random_board(N: int, iterations=100) -> list:
    """
    Returns a scrambled N x N board as a 2D list.
    """
    directions = [(0, 1), (1, 0), (0, -1), (-1, -1)]

    def isLegal(x, y):
        return (x >= 0 and x < N and y >= 0 and y < N)

    def swap(board, hole_x, hole_y, x, y):
        board[hole_y][hole_x], board[y][x] = board[y][x], board[hole_y][hole_x]
        return board, x, y

    # create initial board
    board = [[x + y * N+1 for x in range(N)] for y in range(N)]
    hole_x, hole_y = N-1, N-1
    # scramble the board
    for i in range(iterations):
        direction = random.choice(directions)
        dx, dy = direction
        temp_x, temp_y = hole_x+dx, hole_y+dy
        if (isLegal(temp_x, temp_y)):
            board, hole_x, hole_y = swap(board, hole_x, hole_y, temp_x, temp_y)

    # replace the hole cell with an empty space
    board[hole_y][hole_x] = N**2  # = " "

    return board


def display_board(board):
    """
    Displays the board in a nicely formatted 3x3 array.
    """
    for row in board:
        print("|".join([f"{str(cell):^4}" for cell in row]))


def to_one_dimension(board) -> list:
    return [value for row in board for value in row]


if __name__ == "__main__":
    board = get_random_board(6, 100000)
    display_board(board)
    print(to_one_dimension(board))
