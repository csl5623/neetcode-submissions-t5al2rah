class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        n = len(position)
        cars = []
        for i in range(n):
            cars.append([position[i],speed[i]])
        sortedCars = sorted(cars)
        stack = []
        for i in range(n - 1, -1, -1):
            curr = sortedCars[i]
            stack.append(curr)
            if len(stack) >= 2:
                value1 = stack[-1]
                value2 = stack[-2]
                res1 = (target - value1[0]) / value1[1]
                res2 = (target -  value2[0]) / value2[1]
                if res1 <= res2:
                    stack.pop()
        return len(stack)

