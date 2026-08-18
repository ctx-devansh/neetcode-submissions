class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # make dictionary where key is num 
        # value is count of that number in nums
        counts = {}
        for num in nums:
            counts[num] = 1 + counts.get(num,0)

        # Use the counts dictionary to build
        # dictionary where key is frequency
        # value is a list of all nums which have that frequency in nums
        frequency_key = defaultdict(list)
        for num in counts.keys():
            frequency_key[counts[num]].append(num)
        
        # Max frequency possible is len(nums)
        # For Top K most start looking up in frequency key dictionary from len(nums). 
        # Keep appending numbers in result array until k elements added
        result = []
        for i in range(len(nums),-1,-1):
            while len(result) < k and frequency_key[i]:
                result.append(frequency_key[i].pop())
        return result
        