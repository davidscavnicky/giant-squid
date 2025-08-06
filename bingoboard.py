class BingoBoard:
    def __init__(self, grid):
        """
        Initialize the Bingo board with a 5x5 grid of numbers.
        `grid` is a list of lists containing integers.
        We also create a 5x5 boolean matrix `marked` to track marked numbers.
        """
        self.marked = [[False]*5 for _ in range(5)]  # initially no numbers are marked
        self.grid = grid  # store the board numbers

    def marked_numbers(self, number):
        """
        Mark the integers on the board if it exists based on given numbers.
        """
        for i in range(5):
            for j in range(5):
                if self.grid[i][j] == number:
                    self.marked[i][j] = True

    def winning_condition(self):
        """
        Check if the board has a winning condition.
        A winning condition is met if any row, column is fully marked. Diagonals don't count.
        """
        # Check all rows
        for row in self.marked:
            if all(row): 
                return True

        # Check all columns by transposing original matrix
        for col in zip(*self.marked):
            if all(col):
                return True

        return False

    def unmarked_sum(self):
        """
        Accumulative sum of unmarked numbers on the board. = Final score
        """
        total = 0
        for i in range(5):
            for j in range(5):
                if not self.marked[i][j]:
                    total += self.grid[i][j]
        return total
