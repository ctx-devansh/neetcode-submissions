class Solution:
    def sortColors(self, nums: List[int]) -> None:
        counts = [0] * 3

        for num in nums:
            counts[num] += 1
        print(counts)

        i = 0
        for num in range(0,3):
            for count in range(counts[num]):
                nums[i] = num
                i += 1
        