class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums) - 1
        l = 0
        nums.sort()
        res = []

        while l < n - 1:
            r = l + 1
            while r <= n:
                target = 0 - (nums[l] + nums[r])
                if r < n and target in nums[r + 1:]:
                    triplet = [nums[l], nums[r], target]
                    if triplet not in res:
                        res.append(triplet)
                r += 1
            l += 1
        
        return res
               