import bingoboard

# Solve Advent of Code Day 4: Giant Squid (Part 1)
with open('input.txt', 'r') as f:
    input_str = f.read()

draws, boards = bingoboard.parse_input(input_str)
final_score = bingoboard.run_bingo_simulation(draws, boards)

print(f"Final Score: {final_score}")