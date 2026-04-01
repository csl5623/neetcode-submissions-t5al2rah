class Solution:
    def generate_key(self,d):
        s = sorted(d)
        k = ""
        for i in s:
            k+=i
        return k

    def isAnagram(self,s,t):
        if len(s) != len(t):
            return False
        
        return sorted(s) == sorted(t)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        for i in strs:
            key = self.generate_key(i)
            if key in anagram_map:
                anagram_map[key].append(i)
            else:
                anagram_map[key] = [i]
        result = []
        for i in anagram_map.values():
            result.append(i)
        return result

            