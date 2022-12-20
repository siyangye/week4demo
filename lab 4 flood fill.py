#!/usr/bin/env python
# coding: utf-8

# In[15]:


from typing import List

board = [
    "......................",
    "......##########......",
    "......#........#......",
    "......#........#......",
    "......#........#####..",
    "....###............#..",
    "....#............###..",
    "....##############....",
]

def flood_fill(input_board: List[str], old: str, new: str, x: int, y: int) -> List[str]:
    if not 0<= x < len(input_board) or not 0 <= y < len(input_board[0]) or old!= input_board[x][y]:
        return input_board
    if input_board[x][y] == '#' or input_board[x][y]== new:
    # the logic of if not- if 
        return input_board 
    elif input_board[x][y] == '.':
        input_board[x] = input_board[x][0:y]+'~'+ input_board[x][y+1:]
        if x >=1 :
            flood_fill(input_board, old, new, x-1, y)
        if x <= len(input_board) :
            flood_fill(input_board, old, new, x+1, y)
        if y >= 1:
            flood_fill(input_board, old, new, x, y-1)
        if y <= len(input_board[0]):
            flood_fill(input_board, old, new, x, y+1)
    input_board[x] = input_board[x][:y] + new + input_board[x][y+1:]
    
    return input_board 
            
    
    """Returns board with old values replaced with new values
    through flood filling starting from the coordinates x, y
    Args:
        input_board (List[str])
        old (str): Value to be replaced
        new (str): Value that replaces the old
        x (int): X-coordinate of the flood start point
        y (int): Y-coordinate of the flood start point
    Returns:
        List[str]: Modified board
    """



modified_board = flood_fill(input_board=board, old=".", new="~", x=5, y=12)

for a in modified_board:
    print(a)

# Expected output:
# ......................
# ......##########......
# ......#~~~~~~~~#......
# ......#~~~~~~~~#......
# ......#~~~~~~~~#####..
# ....###~~~~~~~~~~~~#..
# ....#~~~~~~~~~~~~###..
# ....##############....