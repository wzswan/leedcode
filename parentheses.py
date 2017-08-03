class Solution(object):
    def lengthOfLongestSubstring(self, s):
        ans = 0
        # left is used to mark leagl left position, Last is ued to record the last appear time
        left = 0
        last = {}
        for i in range(len(s)):
            # when string appear duplicated char, change left to the last s[i] position, make the sting is legal
            if s[i] in last and last[s[i]] >= left:
                left = last[s[i]] + 1
            last[s[i]] = i
            ans = max(ans, i - left + 1)
    return ans
