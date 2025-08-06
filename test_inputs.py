import bingoboard

def test_input_file(filename, expected_part1=None, expected_part2=None):
    """Test a specific input file for both Part 1 and Part 2"""
    print(f"\n=== Testing {filename} ===")
    
    try:
        with open(filename, 'r') as f:
            input_data = f.read()
        
        # Test Part 1
        draws, boards = bingoboard.parse_input(input_data)
        result_part1 = bingoboard.run_bingo_simulation(draws, boards)
        
        print(f"Number of draws: {len(draws)}")
        print(f"Number of boards: {len(boards)}")
        print(f"Part 1 score: {result_part1}")
        
        if expected_part1:
            print(f"Part 1 expected: {expected_part1}")
            print(f"Part 1 test passed: {result_part1 == expected_part1}")
        
        # Test Part 2 (need fresh boards)
        draws, boards = bingoboard.parse_input(input_data)
        result_part2 = bingoboard.run_bingo_simulation_part2(draws, boards)
        
        print(f"Part 2 score: {result_part2}")
        
        if expected_part2:
            print(f"Part 2 expected: {expected_part2}")
            print(f"Part 2 test passed: {result_part2 == expected_part2}")
        
        return result_part1, result_part2
        
    except Exception as e:
        print(f"Error testing {filename}: {e}")
        return None, None

if __name__ == "__main__":
    # Test example input (Part 1: 4512, Part 2: 1924)
    test_input_file('inputexample.txt', expected_part1=4512, expected_part2=1924)
    
    # Test actual input (Part 1: 51776, Part 2: 16830)
    test_input_file('input.txt', expected_part1=51776, expected_part2=16830)
