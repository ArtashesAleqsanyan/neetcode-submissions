class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        boxes = [set() for _ in range(n)]
        for i in range(n):
            ##cheking rows
            seen1 = set()
            for ch in board[i]:
                if ch in seen1 and ch != ".":
                    return False
                seen1.add(ch)
            ##checking columns
            seen2 = set()
            for j in range(n): 
                if board[j][i] != "." and board[j][i] in seen2:
                    return False
                seen2.add(board[j][i]) 
            ##checking squares
            for j in range(n): 
                if board[i][j] == ".":
                    continue
                else:
                    val = int(board[i][j])
                    box_idx = (i // 3) * 3 + (j // 3)
                    if val in boxes[box_idx]:
                        return False
                    boxes[box_idx].add(val)
        return True