class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        i = 0
        while i < len(nums):
            lg = lookup.get(nums[i])
            if lg is None:
                lookup[target-nums[i]] = i
            else:
                return [lg, i]
            i+=1

        