class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def validGroup(nums: List[str]) -> bool:
            dig_map = defaultdict(int)
            for num in nums:
                dig_map[num] += 1
            if '.' in dig_map: del dig_map['.']

            # check for duplicates
            values = set(list(dig_map.values()))
            if len(values) != 0 and values != {1}: return False

            # check theyre all between 1-9
            for key in dig_map:
                if int(key) not in range(1, 10): return False
                    
            return True

        # checking rows
        for row in board:
            if not validGroup(row): return False
        
        # checking cols
        for col_i in range(9):
            col = [board[row_i][col_i] for row_i in range(9)]
            if not validGroup(col): return False
        
        # checking sub-boxes
        for box_row in range(3):
            for box_col in range(3):
                box = []
                for row_i in range(box_row*3, box_row*3 + 3):
                    for col_i in range(box_col*3, box_col*3 + 3):
                        box.append(board[row_i][col_i])
                if not validGroup(box): return False
        
        return True