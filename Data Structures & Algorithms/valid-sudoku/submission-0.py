"""
Understanding:
    Input: 9 by 9 array of digits 1-9 or "."
    Output: True if the baord is valid sudoku
            False if the board is not valid sudoku
        
    - Each column, row and 3 by 3 square must only contain one digit of its kind 
    - "." represents the lack of a value

Match:
    - Hash Table
    
Planning:
    - Iterate through each row of the array
        - Declare a dict that will keep track of the numbers seen in a 3 by 3 sub box
        - Declare a dict that will keep track of values in a colum
           (keys are colum indices, values are sets of the values in that colum)
        - Iterate through each column of the array
            -  check what 3 by 3 box this box lies in
                if the value at this square already exists: return False
            - If this value exists in the same column: return Fale else add to colum set

   0   1   2   3   4   5   6   7   8       rows
[["1","2",".",".","3",".",".",".","."], 0 {1,2,3}   {1,4,5,7}
 ["4",".",".","5",".",".",".",".","."], 1 {4,5}     {2,9}
 [".","9","1",".",".",".",".",".","3"], 2 {9,1,3}   {1}
 ["5",".",".",".","6",".",".",".","4"], 3 {5,6}     {5,8,4}
 [".",".",".","8",".","3",".",".","5"], 4 {8,3,5}   {3,6,2,1,8}
 ["7",".",".",".","2",".",".",".","6"], 5 {7,2,6}   {3,9}
 [".",".",".",".",".",".","2",".","."], 6 {2}       {2}
 [".",".",".","4","1","9",".",".","8"], 7 {4,1,9,8} {7}
 [".",".",".",".","8",".",".","7","9"]] 8 {8,7,9}   {3,4,5,6,8,9}
"""
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = {i: set() for i in range(len(board))}
        rows = {i: set() for i in range(len(board))}
        squares = collections.defaultdict(set)

        for row in range(len(board)):
            for col in range(9):
                value = board[row][col]
                if value == ".":
                    continue
                sqr_idx = (row//3, col//3)
                sqr = squares.get(sqr_idx, set())
                if value in cols[col] or value in rows[row] or value in sqr:
                    return False
                
                squares[sqr_idx].add(value)
                rows[row].add(value)
                cols[col].add(value)
            
        return True
                