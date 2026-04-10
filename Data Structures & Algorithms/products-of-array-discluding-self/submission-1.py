class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ##non optimal solution
        product_of_array = []
        for i in range(len(nums)):
            current_product = 1
            for j in range(len(nums)):
                if i != j:
                    current_product *= nums[j]
            product_of_array.append(int(current_product))
        return product_of_array
