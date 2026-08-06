from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkList(inpList):
                numDict = defaultdict(int)
                for num in inpList: # checking that there are no duplicate nums in any row
                    numDict[num] += 1
                    # 1: 1
                    # 2: 1
                    # 3: 0
                    # 4: 1
                    # .: 6
                for key, val in numDict.items():
                    if key != "." and val > 1:
                        return False
                return True
        
        def getSubSq(bigRow, bigCol):
            subSqList = []
            for row in range(bigRow, bigRow + 3):
                for col in range(bigCol, bigCol + 3):
                    subSqList.append(board[row][col])
            return subSqList


        for row in board:
            if not checkList(row):
                return False
            

        
        for colnum in range(9):
            col = []
            for rownum in range(9):
                col.append(board[rownum][colnum])
            if not checkList(col):
                return False

        for bigRow in [0, 3, 6]: 
            for bigCol in [0, 3, 6]:
                if not checkList(getSubSq(bigRow, bigCol)):
                    return False


        return True
            


            