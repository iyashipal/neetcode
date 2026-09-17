class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check rows, columns and square at the same time for each value
        '''    row = defaultdict(set)
            col = defaultdict(set)
            sq = defaultdict(set)

            for r in range(9):
                for c in range(9):
                    if board[r][c] == ".":
                        continue
                    if (board[r][c] in row[r] 
                    or board[r][c] in col[c] 
                    or board[r][c] in sq[r//3, c//3]):
                        return False

                    col[c].add(board[r][c])
                    row[r].add(board[r][c])
                    sq[r//3,c//3].add(board[r][c])

            return True
                '''

        #use arrays and bits, saves space and no iteration required since we can use bitwise "and" and "or" operations for validation
        row = [0] * 9
        col = [0] * 9
        sq = [0] * 9

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                
                val = int(board[r][c]) - 1

                if((1<<val)&row[r]) or ((1<<val)&col[c]) or ((1<<val)&sq[(r//3)*3+(c//3)]):
                    return False

                row[r] |= (1<<val)
                col[c] |= (1<<val)
                sq[(r//3)*3+(c//3)] |= (1<<val)

        return True