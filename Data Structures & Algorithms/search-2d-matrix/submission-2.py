class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        extended_matrix = list()
        ##brute force: create a single array and then use binary search 
        for row in matrix:
            for element in row:
                extended_matrix.append(element)
        
        m = len(extended_matrix)
        l = 0
        r = len(extended_matrix) -1

        while l <= r:
            mid = (l+r) //2
            if extended_matrix[mid] == target:
                return True
            elif extended_matrix[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False
        



