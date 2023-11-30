
#find point where bishop and knight can meet

from collections import deque

# user input

bishopStart = (3,2)
horseStart = (6,6)
invalid = set([(2,3),(4,3),(2,1),(3,3)])

def is_valid_move(x, y):
    return 1 <= x <= 7 and 1 <= y <= 7

    
visitedbyhorse = set()
visitedbybishop = set()

def solve():

    horseQ = deque([horseStart])
    bishopQ = deque([bishopStart])
    
    
    
    while horseQ or bishopQ:
        
        if horseQ :
            start_x , start_y = horseQ.popleft()
            moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
            for move in moves:
                new_x = start_x + move[0]
                new_y = start_y + move[1]
            
                    
                if is_valid_move(new_x, new_y) and not (new_x, new_y) in visitedbyhorse  and not (new_x, new_y) in invalid:
                    
                    if (new_x,new_y) in visitedbybishop:
                        return f"they can meet @ {(new_x,new_y)}"
                        
                    horseQ.append((new_x, new_y))
                    visitedbyhorse.add((new_x, new_y))
                    
                    
            
        if bishopQ:
            start_x , start_y = bishopQ.popleft()
            moves = [(1, -1), (-1, 1), (-1, -1), (1, 1)]
            
            for move in moves:
                new_x = start_x + move[0]
                new_y = start_y + move[1]
                
                    
                if is_valid_move(new_x, new_y) and not (new_x, new_y) in visitedbybishop and not (new_x, new_y) in invalid: 
                    
                    if (new_x,new_y) in visitedbyhorse:
                        return f"they can meet @ {(new_x,new_y)}"
                    
                    horseQ.append((new_x, new_y))
                    visitedbybishop.add((new_x, new_y))
        
    return "No valid points to meet"

print(solve())
        
    
    
    
    
    
    
    