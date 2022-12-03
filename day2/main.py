MOVE_INT_MAP = {
    "A": 0,
    "B": 1,
    "C": 2,
    "X": 0,
    "Y": 1,
    "Z": 2 
}

"""
0 == Rock 
1 == Paper 
2 == Scissors 

1 > 0, 2 > 1, 0 > 2

(0-1) % 3 
"""

class RPSMove: 
    def __init__(self, letter=None, number=None) -> None:
        if letter:
            self.move_choice = MOVE_INT_MAP[letter]
        else: 
            self.move_choice = number
        
    def is_beating(self, opposing_move) -> bool: 
        return (self.move_choice - 1) % 3 == opposing_move.move_choice
    
    def __str__ (self) -> str: 
        return str(self.move_choice)
    
    def __eq__(self, opposing_move: object) -> bool:
        return opposing_move.move_choice == self.move_choice
    
    
    
def calculate_move_score_part1(my_move, their_move): 
    score = my_move.move_choice + 1 
    if my_move == their_move: 
        score += 3 
    elif my_move.is_beating(their_move): 
        score += 6 
    
    return score 

def calculate_move_score_part2(my_move, their_move): 
    """
    0 == Lose 
    1 == Draw 
    2 == Win 
    """
    
    my_new_move = None 
    
    if my_move.move_choice == 0:
        # Lose
        my_new_move = RPSMove(number=((their_move.move_choice - 1) % 3)) 
    elif my_move.move_choice == 1: 
        # Draw
        my_new_move = their_move
    else: 
        # Win
        my_new_move = RPSMove(number=((their_move.move_choice + 1) % 3)) 
    
    return calculate_move_score_part1(my_new_move, their_move)
        
    

def parse_input():
    """
    Generate a list of moves in RPS game.
    """
    moves = list() 
    with open('day2/input.txt') as f:
        lines = f.readlines()
        
        for line in lines: 
            raw_moves = line.split()
            moves.append([RPSMove(raw_moves[0]), RPSMove(raw_moves[1])])
        
        return moves 
    
moves = parse_input() 

# Part one 
total_score = 0 
for move in moves: 
    total_score += calculate_move_score_part1(move[1], move[0])

print(f"Part one: {total_score} score")


# Part two
total_score = 0 
for move in moves: 
    total_score += calculate_move_score_part2(move[1], move[0])

print(f"Part two: {total_score} score")