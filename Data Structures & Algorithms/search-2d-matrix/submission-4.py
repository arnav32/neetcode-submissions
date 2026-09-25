class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        l, r, mid = 0, (m*n)-1, (m*n)//2
        getMtx = lambda i : matrix[i//n][i%n]
        while l <= r:
            mid = (l+r)//2
            if target < getMtx(mid):
                r = mid-1
            elif target > getMtx(mid):
                l = mid+1
            else:
                return True
        return False

