class Solution:
    def sortColors(self, nums: List[int]) -> None:
        self.divide(nums, 0, len(nums)-1)


    def divide(self, nums: List[int], l: int, r: int) -> None:
        if l == r:
            return
        else:
            m = (l+r)//2
            self.divide(nums, l, m)
            self.divide(nums, m+1, r)
            self.merge(nums, l, m , r)

    def merge(self, nums: List[int], l: int, m: int, r: int) -> None:
        left = nums[l:m+1]
        right = nums[m+1:r+1]
        i, j, k = l,0,0

        while j < len(left) and k < len(right):
            if left[j] < right[k]:
                nums[i] = left[j]
                j += 1
            elif right[k] < left[j]:
                nums[i] = right[k]
                k += 1
            else:
                nums[i] = left[j]
                j += 1
                i += 1
                nums[i] = right[k]
                k += 1
            i += 1
        
        while j < len(left):
            nums[i] = left[j]
            j += 1
            i += 1
        
        while k < len(right):
            nums[i] = right[k]
            k += 1
            i += 1
        