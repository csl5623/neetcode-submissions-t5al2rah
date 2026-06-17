class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        max_area = 0
        stack = []
        for i in range(len(heights)):
            start = i
            if stack:
                top_element = stack[-1]
                while stack and top_element[1] > heights[i]:
                    curr_area = (i - top_element[0]) * top_element[1]
                    max_area = max(max_area,curr_area)
                    start = top_element[0]
                    stack.pop()
                    if stack:
                       top_element = stack[-1]
            stack.append([start,heights[i]])
        
        for i,h in stack:
            max_area = max(max_area,h* (len(heights)-i))
        return max_area
                
