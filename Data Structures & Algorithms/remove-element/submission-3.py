class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i  = 0
        k  = 0
        first_pointer = 0
        # Go through all elements in the nums array
        while i < len(nums):
            # If the current element beign checked is the val to remove
            # Set this position for swapping
            if nums[i] == val:
                first_pointer = i
                second_pointer = i + 1
                # Look for the first element to swap that is not val to remove
                while second_pointer < len(nums) and nums[second_pointer] == val:
                    second_pointer += 1
                # If we reached len(nums) then all occurences of val have been removed
                # or moved to end of nums array in this case hence RETURN
                # else swap
                if second_pointer < len(nums):
                    temp = nums[second_pointer]
                    nums[second_pointer] = nums[first_pointer]
                    nums[first_pointer] = temp
                else:
                    break
            i += 1
            k += 1
        return k
            
