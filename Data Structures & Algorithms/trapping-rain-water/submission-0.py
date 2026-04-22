class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)

        for i in range(1,len(height)):
            if height[i-1] > maxLeft[i-1]:
                maxLeft[i] = height[i-1]
            else:
                maxLeft[i] = maxLeft[i-1]
        for i in range(len(height)-2,-1,-1):
            if height[i+1] > maxRight[i+1]:
                maxRight[i] = height[i+1]
            else:
                maxRight[i] = maxRight[i+1]
        print(maxLeft)
        print(maxRight)
        total_water_trapped = 0
        for i in range(len(height)):
            current_area = min(maxLeft[i],maxRight[i]) - height[i]
            if current_area > 0:
                total_water_trapped += current_area
        return total_water_trapped
