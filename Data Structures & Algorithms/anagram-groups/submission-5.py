class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for str in strs:
            letters = "".join(sorted(str))
            if letters in anagrams:
                anagrams[letters].append(str)
            else:
                anagrams[letters] = [str]
        
        return list(anagrams.values())