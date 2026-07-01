class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows_seen = [[False] * 9 for _ in range(9)]
        cols_seen = [[False] * 9 for _ in range(9)]
        boxes_seen = [[False] * 9 for _ in range(9)]
        for row_idx in range(9):
            for col_idx in range(9):
                cell_value = board[row_idx][col_idx]

                if cell_value == '.':
                    continue
                digit_idx = int(cell_value) - 1
                box_idx = (row_idx // 3) * 3 + (col_idx // 3)
                if (rows_seen[row_idx][digit_idx] or 
                    cols_seen[col_idx][digit_idx] or 
                    boxes_seen[box_idx][digit_idx]):
                    return False
                rows_seen[row_idx][digit_idx] = True
                cols_seen[col_idx][digit_idx] = True
                boxes_seen[box_idx][digit_idx] = True
        return True
