class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = 1 + counts.get(num,0)

        frequency_key = defaultdict(list)
        for num in counts.keys():
            frequency_key[counts[num]].append(num)
        
        result = []
        for i in range(len(nums),-1,-1):
            while len(result) < k and frequency_key[i]:
                result.append(frequency_key[i].pop())
        return result
        