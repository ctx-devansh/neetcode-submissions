class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = []
        left = 1
        for num in nums:
            products.append(left)
            left *= num
        right = 1
        for i in range(len(nums)-1,-1,-1):
            products[i] *= right
            right *= nums[i]
        return products