class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)
        count = 0
        for num in nums:
            if num-1 not in hashSet:
                curr_count = 1
                while (num+1) in hashSet:
                    curr_count+=1
                    num+=1
                count = max(count, curr_count)
        return count
