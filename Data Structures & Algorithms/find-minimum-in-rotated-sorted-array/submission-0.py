class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while nums[r] < nums[l]:
            mid = (l + r) // 2

            if nums[mid] < nums[l]:
                r = mid
            elif nums[mid] >= nums[l]:
                l = mid + 1

        return nums[l]