import unittest
import bingoboard

class TestBingoBoard(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures before each test method"""
        self.test_grid = [
            [22, 13, 17, 11, 0],
            [8, 2, 23, 4, 24],
            [21, 9, 14, 16, 7],
            [6, 10, 3, 18, 5],
            [1, 12, 20, 15, 19]
        ]
        self.board = bingoboard.BingoBoard(self.test_grid)
    
    def test_board_initialization(self):
        # Check grid is stored correctly
        self.assertEqual(self.board.grid, self.test_grid)
        
        # Check all positions are initially unmarked
        for row in self.board.marked:
            for cell in row:
                self.assertFalse(cell)
  
    def test_winning_condition_row(self):
        # Mark entire first row
        for num in [22, 13, 17, 11, 0]:
            self.board.marked_numbers(num)
        
        self.assertTrue(self.board.winning_condition())
    
    def test_winning_condition_column(self):
        # Mark entire first column
        for num in [22, 8, 21, 6, 1]:
            self.board.marked_numbers(num)
        
        self.assertTrue(self.board.winning_condition())
    
    def test_no_winning_condition(self):
        # Mark 4 out of 5 in first row
        for num in [22, 13, 17, 11]:
            self.board.marked_numbers(num)
        
        self.assertFalse(self.board.winning_condition())
    
    def test_unmarked_sum(self):
        # Initially, all numbers should be unmarked
        expected_sum = sum(sum(row) for row in self.test_grid)
        self.assertEqual(self.board.unmarked_sum(), expected_sum)
        
        # Mark some numbers and check sum
        self.board.marked_numbers(22)  # Mark 22
        self.board.marked_numbers(13)  # Mark 13
        expected_sum = expected_sum - 22 - 13
        self.assertEqual(self.board.unmarked_sum(), expected_sum)

class TestBingoSimulation(unittest.TestCase):

    def setUp(self):
        with open("inputexample.txt", "r") as f:
            self.example_input = f.read()

    def test_parse_input(self):
        draws, boards = bingoboard.parse_input(self.example_input)

        # Check draws are parsed correctly
        expected_draws = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
        self.assertEqual(draws, expected_draws)

        # Check correct number of boards
        self.assertEqual(len(boards), 3)

        # Check first board's first row
        expected_first_row = [22, 13, 17, 11, 0]
        self.assertEqual(boards[0].grid[0], expected_first_row)

    def test_empty_input_handling(self):
        draws, boards = bingoboard.parse_input("1,2,3\n\n1 2 3 4 5\n6 7 8 9 10\n11 12 13 14 15\n16 17 18 19 20\n21 22 23 24 25")

        self.assertEqual(len(draws), 3)
        self.assertEqual(len(boards), 1)
        self.assertEqual(len(boards[0].grid), 5)
        self.assertEqual(len(boards[0].grid[0]), 5)


class TestBingoBoardEdgeCases(unittest.TestCase):
    
    def test_all_numbers_marked(self):
        """Test when all numbers on board are marked"""
        grid = [[i + j * 5 + 1 for i in range(5)] for j in range(5)]
        board = bingoboard.BingoBoard(grid)
        
        # Mark all numbers
        for row in grid:
            for num in row:
                board.marked_numbers(num)
        
        self.assertTrue(board.winning_condition())
        self.assertEqual(board.unmarked_sum(), 0)


if __name__ == '__main__':
    unittest.main(verbosity=2)
