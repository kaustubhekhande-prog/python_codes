def safe(board, row, col):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True


def solve(board, row, n):
    if row == n:
        for i in range(n):
            for j in range(n):
                print("Q" if board[i] == j else ".", end=" ")
            print()
        return True

    for col in range(n):
        if safe(board, row, col):
            board[row] = col
            if solve(board, row + 1, n):
                return True
    return False


def run():
    n = int(input("Enter number of queens: "))
    if n <= 0:
        print("Enter a positive number.")
        return

    board = [-1] * n
    if not solve(board, 0, n):
        print("No solution exists")


if __name__ == "__main__":
    run()
