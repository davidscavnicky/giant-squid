def __init__(self, grid):
        self.marked = [[False]*5 for _ in range(5)]  # initially no numbers are marke
        self.grid = grid  # store the board numbers

def marker(self, number):
        for i in range(5):
            for j in range(5):
                if self.grid[i][j] == number:
                    self.marked[i][j] = True
