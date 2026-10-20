class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [[1,0], [0,1], [-1,0], [0,-1]]
        seen = set()

        def dfs(r, c, target):
            if not target:
                return True
            
            if (r, c) in seen or r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or board[r][c] != target[0]:
                return
            
            target = target[1:]
            seen.add((r, c))
            for dr, dc in directions:
                if dfs(r + dr, c + dc, target):
                    return True
            seen.remove((r, c))
            return False

        for r in range(len(board)):
            for c in range(len(board[r])):
                if dfs(r, c, word):
                    return True
        return False