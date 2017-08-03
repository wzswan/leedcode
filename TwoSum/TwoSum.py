class Solution(object):
    def TwoSum(self, nums, target):
        k = 0
        for i in nums:
            j = target - i
            k += 1
            tmp_nums = nums[k:]
            if j in tmp_nums:
                return[k-1, tmp_nums.index(j) + k]

if __name__ =='__main__':
    print Solution().TwoSum((2,7,11,15),9)
