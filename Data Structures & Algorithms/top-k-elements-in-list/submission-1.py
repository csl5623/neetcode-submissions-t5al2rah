class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        indexArray = [[] for _ in range(len(nums)+1)]
        print(indexArray)
        countMap = dict()
        for i in nums:
            if i in countMap:
                countMap[i] +=1
            else:
                countMap[i] = 1
        print(countMap)
        
        for i in countMap:
            index = countMap[i]
            indexArray[index].append(i)

        
        print(indexArray)
        list_k_items = []
        for i in range(len(indexArray)-1,-1,-1):
            for value in indexArray[i]:
                if len(list_k_items) < k:
                    list_k_items.append(value)
        return list_k_items

        

        

        
        



             
        
        



            