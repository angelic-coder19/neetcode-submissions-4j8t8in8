class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums) - 1
        l, r = 0, n
        while nums[l] > nums[r]:
            mid = (l + r) // 2

            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid
        
        if l != 0 and nums[0] <= target <= nums[l - 1]:
            high, low = l - 1, 0
        else:
            high, low = n, l
        
        while high >= low:
            m = (high + low) // 2

            if nums[m] == target:
                return m
            
            elif target > nums[m]:
                low = m + 1
            else:
                high = m - 1
        
        return -1
            
