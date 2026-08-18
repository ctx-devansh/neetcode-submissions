class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = 1 + counts.get(num,0)

        frequency_key = defaultdict(list)
        for num in counts.keys():
            frequency_key[counts[num]].append(num)
        
        result = []
        result_len = 0
        for i in range(len(nums),-1,-1):
            num_list = frequency_key[i]
            while result_len < k and len(num_list) > 0:
                result.append(num_list.pop())
                result_len += 1
        return result
        