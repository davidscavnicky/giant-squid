import bingoboard

def test_part1(filename, expected=None):
    """Test Part 1 (first winner) for a specific input file"""
    with open(filename, 'r') as f:
        input_data = f.read()
    
    draws, boards = bingoboard.parse_input(input_data)
    result = bingoboard.run_bingo_simulation(draws, boards)
    
    print(f"Part 1 - {filename}: {result}")
    if expected:
        passed = result == expected
        print(f"  Expected: {expected} | {'PASS' if passed else 'FAIL'}")
    
    return result

def test_part2(filename, expected=None):
    """Test Part 2 (last winner) for a specific input file"""
    with open(filename, 'r') as f:
        input_data = f.read()
    
    draws, boards = bingoboard.parse_input(input_data)
    result = bingoboard.run_bingo_simulation_part2(draws, boards)
    
    print(f"Part 2 - {filename}: {result}")
    if expected:
        passed = result == expected
        print(f"  Expected: {expected} | {'PASS' if passed else 'FAIL'}")
    
    return result

def test_all():
    """Run all tests for both parts"""
    print("Running Advent of Code Day 4 Tests\n")
    
    # Test example input
    print("=== Example Input Tests ===")
    test_part1('inputexample.txt', 4512)  # Expected Part 1 result - given example and final result
    test_part2('inputexample.txt', 1924)  # Expected Part 2 result - calculated by algo and check against website

    print("\n=== Actual Input Tests ===")
    test_part1('input.txt', 51776)  # Expected Part 1 result - given example and final result
    test_part2('input.txt', 16830)  # Expected Part 2 result

    print("\nAll tests completed!")

if __name__ == "__main__":
    test_all()
