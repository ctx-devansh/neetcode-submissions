class Solution:
    def sortColors(self, nums: List[int]) -> None:
        zero = 0
        two = len(nums) - 1
        i = 0
        while i < len(nums):
            if i >= zero and nums[i] == 0:
                temp = nums[zero]
                nums[zero] = nums[i]
                nums[i] = temp
                zero += 1
            elif i <= two and nums[i] == 2:
                temp = nums[two]
                nums[two] = nums[i]
                nums[i] = temp
                two -= 1
                continue
            i += 1
            

        
        