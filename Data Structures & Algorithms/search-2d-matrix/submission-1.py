class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        array = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                array.append(matrix[i][j])
        
        return self.innerbinary(0,len(array)-1,array,target)
    
    
    def innerbinary(self,l,r,matrix,target):
        if l > r:
            return False
        mid = l + (r-l) //2
        if matrix[mid] == target:
            return True
        elif matrix[mid] > target:
            return self.innerbinary(l,mid-1,matrix,target)
        else:
            return self.innerbinary(mid+1,r,matrix,target)
        



