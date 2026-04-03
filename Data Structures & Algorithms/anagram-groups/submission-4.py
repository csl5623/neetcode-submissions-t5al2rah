class Solution:
    def generate_key(self,s):
        sortedString =  "".join(sorted(s))
        return sortedString
        
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = dict()
        for i in strs:
            key = self.generate_key(i)
            print(key)
            if key in anagramMap:
                anagramMap[key].append(i)
            else:
                anagramMap[key] = [i]
        
        return list(anagramMap.values())

        