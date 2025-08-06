import bingoboard

# Solve Advent of Code Day 4: Giant Squid
with open('input.txt', 'r') as f:
    input_str = f.read()

# Part 1: Find the first winner
draws, boards = bingoboard.parse_input(input_str)
final_score_part1 = bingoboard.run_bingo_simulation(draws, boards)
print(f"Part 1 - First Winner Score: {final_score_part1}")

# Part 2: Find the last winner (need fresh boards since Part 1 modified them)
draws, boards = bingoboard.parse_input(input_str)
final_score_part2 = bingoboard.run_bingo_simulation_part2(draws, boards)
print(f"Part 2 - Last Winner Score: {final_score_part2}")