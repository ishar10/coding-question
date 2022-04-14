'''Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.'''


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        block=collections.defaultdict(set)
        row=collections.defaultdict(set)
        col=collections.defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j]==".":
                    continue
                elif (board[i][j] in row[i]) or (board[i][j] in col[j]) or (board[i][j] in block[(i//3,j//3)]) :
                        return False
                else:
                    row[i].add(board[i][j])
                    col[j].add(board[i][j])
                    block[(i//3,j//3)].add(board[i][j])
        return True