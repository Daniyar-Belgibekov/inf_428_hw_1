class Solution(object):
    def findLengthOfLCIS(self, nums):
        max_l = 1
        length = 1

        if not nums:
            return 0

        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                length += 1
                max_l = max(max_l, length)
            else:
                length = 1

        return max_l