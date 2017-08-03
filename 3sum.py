class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        res = []
        length = len(nums)
        for i in range(0, length -2):
            if i and nums[i] == nums[i -1]: # jump the same num part
                continue
            target = nums[i] * -1
            left, right = i + 1, length -1
            while left < right:
                if nums[left] + nums[right] == target:
                    res.append([nums[i], nums[left], nums[right]])
                    right -= 1
                    left += 1
                    while left < right and nums[left] == nums[left -1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif nums[left] + nums[right] > target:
                    ritht -= 1
                else:
                    left += 1
    return res
