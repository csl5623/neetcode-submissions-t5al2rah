class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ##right will be the len of matrix
        rows = len(matrix)
        columns = len(matrix[0])
        r = rows  * columns - 1
        l = 0

        ##calculate mid but mid will give number as if the whole matrix is array
        ##For any mid index m, we can map it back to the matrix using:
            ##row = mid // cols
            ##col = m % COLS
        while l <= r:
            mid = (l+r) //2
            row = mid // columns
            col = mid % columns
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False
        



