
def run_bingo_simulation(draws, boards):
    """
    Returns first winner only (Part 1).
    """
    for number in draws:
        for board in boards:
            board.marked_numbers(number)
            if board.winning_condition():
                return board.unmarked_sum() * number
    return None

def run_bingo_simulation_part2(draws, boards):
    """
    Two functions - two logics
    Returns last winner (Part 2).
    Find the board that would win last.
    """
    won_boards = set()  # Track which boards have already won
    
    for number in draws:
        # Mark the number on all boards that haven't won yet
        for i, board in enumerate(boards):
            if i not in won_boards:  # Work on boards that haven't won yet
                board.marked_numbers(number)
                
                if board.winning_condition():
                    won_boards.add(i)
                    
                    # find last board that wins
                    if len(won_boards) == len(boards):
                        return board.unmarked_sum() * number
    
    return None

def parse_input(input_str):
    """
    # This function processes the input for a Bingo game, extracting the sequence of drawn numbers
    # and constructing BingoBoard objects for each board described in the input.
    """
    lines = input_str.strip().split('\n')
    draws = [int(x) for x in lines[0].split(',')]
    boards = []
    current_board = []
    for line in lines[2:]:  # lines[2:] contains the actual Bingo boards
        if line == '':
            boards.append(BingoBoard(current_board))
            current_board = []
        else:
            current_board.append([int(x) for x in line.strip().split()])
    if current_board:
        boards.append(BingoBoard(current_board))
    return draws, boards

class BingoBoard:
    def __init__(self, grid):
        """
        Initialize the Bingo board with a 5x5 grid of numbers.
        `grid` is a list of lists containing integers.
        We also create a 5x5 boolean matrix `marked` to track marked numbers.
        """
        self.marked = [[False]*5 for _ in range(5)]  # initially no numbers are marked = false boolean
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
