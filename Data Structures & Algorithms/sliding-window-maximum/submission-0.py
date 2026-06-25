class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxSlinding = list()
        l = 0
        queue = []
        for r in range(len(nums)):
            queue.append(nums[r])
            while (r -l) + 1 == k:
                max_value = max(queue)
                maxSlinding.append(max_value)
                l+=1
                queue.pop(0)
        return maxSlinding


        