class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_count = 0
        for n in nums:
            if n == 0:
                zero_count += 1
                continue
            product *= n
        
        if zero_count == 0:
            return [product // n for n in nums]
        elif zero_count < 2:
            return [0 if n != 0 else product for n in nums]
        else:
            return [0 for n in nums]
            
