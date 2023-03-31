import random


def get_random_board(N: int, iterations: int = 100) -> list:
    """
    Generate a random NxN board and scramble it.

    Args:
        N (int): The size of the board to be created.
        iterations (int): The amount of iterations used to scramble the board. Defaults to 100.

    Returns:
        list: A scrambled NxN board as a 2D list.

    This function generates a random NxN board with numbers from 1 to N^2-1, 
    and an empty space represented by a " ". It then scrambles the board by
    performing random moves (up, down, left or right) on the empty space for
    a specified number of iterations.
    """
    directions = [(0, 1), (1, 0), (0, -1), (-1, -1)]

    def isLegal(x: int, y: int) -> bool:
        """Check if coordinates x, y are within the bounds of the board."""
        return (0 <= x < N) and (0 <= y < N)

    def swap(board: list, hole_x: int, hole_y: int, x: int, y: int) -> tuple:
        """Swap the empty cell (the hole) with the cell at given position (x, y) in the board."""
        board[hole_y][hole_x], board[y][x] = board[y][x], board[hole_y][hole_x]
        return board, x, y

    # create initial board
    board = [[x + y * N+1 for x in range(N)] for y in range(N)]
    hole_x, hole_y = N-1, N-1
    # Scramble the board using the specified number of iterations
    for i in range(iterations):
        direction = random.choice(directions)
        dx, dy = direction
        temp_x, temp_y = hole_x+dx, hole_y+dy
        if isLegal(temp_x, temp_y):
            board, hole_x, hole_y = swap(board, hole_x, hole_y, temp_x, temp_y)

    board[hole_y][hole_x] = " "

    return board


def display_board(board: list) -> None:
    """
    Display the game board in a table format.

    Args:
        board (list): A 2D list containing ints representing the target position of each cell.

    Returns:
        None
    """
    for row in board:
        print("|".join([f"{str(cell):^4}" for cell in row]))


def to_one_dimension(board) -> list:
    return [value for row in board for value in row]


if __name__ == "__main__":
    board = get_random_board(6, 100000)
    display_board(board)
    print(to_one_dimension(board))
