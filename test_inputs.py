import bingoboard

def test_input_file(filename, expected_result=None):
    """Test a specific input file"""
    print(f"\n=== Testing {filename} ===")
    
    try:
        with open(filename, 'r') as f:
            input_data = f.read()
        
        draws, boards = bingoboard.parse_input(input_data)
        result = bingoboard.run_bingo_simulation(draws, boards)
        
        print(f"Number of draws: {len(draws)}")
        print(f"Number of boards: {len(boards)}")
        print(f"Final score: {result}")
        
        if expected_result:
            print(f"Expected: {expected_result}")
            print(f"Test passed: {result == expected_result}")
        
        return result
        
    except Exception as e:
        print(f"Error testing {filename}: {e}")
        return None

if __name__ == "__main__":
    # Test example input (should give 4512)
    test_input_file('inputexample.txt', 4512)
    
    # Test actual input (should give 51776)
    test_input_file('input.txt', 51776)
