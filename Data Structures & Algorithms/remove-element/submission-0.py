class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i  = 0
        k  = 0
        first_pointer = 0
        while i < len(nums):
            if nums[i] == val:
                first_pointer = i
                second_pointer = i + 1
                while second_pointer < len(nums) and nums[second_pointer] == val:
                    second_pointer += 1
                if second_pointer < len(nums):
                    temp = nums[second_pointer]
                    nums[second_pointer] = nums[first_pointer]
                    nums[first_pointer] = temp
                else:
                    break
            i += 1
            k += 1
        return k
            
