class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        n = len(temperatures)
        
        if n == 1:
            return [0]

        for i in range(n):
            count = 0
            found = False
            for idx, day in enumerate(temperatures[i+1:]):
                if day > temperatures[i]:
                    count = idx + 1
                    found = True
                    break
            
            if not found:
                res.append(0)
            else:
                res.append(count)
        
        return res