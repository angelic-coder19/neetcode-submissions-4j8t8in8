class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l] == nums[r]:
                return nums[l]
            l += 1
            if r - l == 1:
                if nums[l] == nums[r]:
                    return nums[l]
                l = 0
                r -= 1