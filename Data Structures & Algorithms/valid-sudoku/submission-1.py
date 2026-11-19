class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        boxes = [set() for _ in range(n)]
        rows = [set() for _ in range(n)]
        columns = [set() for _ in range(n)]
        for r in range(n):
            for c in range(n):
                if board[r][c] == ".":
                    continue
                val = int(board[r][c])
                box_idx = (r // 3) * 3 + (c // 3)
                if val in boxes[box_idx] or val in rows[r] or val in columns[c]:
                    return False
                boxes[box_idx].add(val)
                rows[r].add(val)
                columns[c].add(val)
        return True
                    

                 

        