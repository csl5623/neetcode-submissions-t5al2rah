class Solution:
    def binary(self,l,r,nums,target):
            if l > r:
                return -1
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                return self.binary(l,mid-1,nums,target)
            else:
                return self.binary(mid + 1,r,nums,target)
    def search(self, nums: List[int], target: int) -> int:
        return self.binary(0,len(nums)-1,nums,target)

