class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        else:
            left_arr = self.sortArray(nums[0:len(nums)//2])
            right_arr = self.sortArray(nums[len(nums)//2:len(nums)])
            return self.mergeRightLeft(right_arr,left_arr)


    def mergeRightLeft(self, right_arr: List[int], left_arr: List[int]):
        out = []
        ri = 0
        li = 0
        while ri < len(right_arr) and li < len(left_arr):
            if right_arr[ri] < left_arr[li]:
                out.append(right_arr[ri])
                ri += 1
            elif right_arr[ri] > left_arr[li]:
                out.append(left_arr[li])
                li += 1
            else:
                out.append(right_arr[ri])
                ri += 1
                out.append(left_arr[li])
                li += 1
        
        while ri < len(right_arr):
            out.append(right_arr[ri])
            ri += 1
        while li < len(left_arr):
            out.append(left_arr[li])
            li += 1
        return out
        