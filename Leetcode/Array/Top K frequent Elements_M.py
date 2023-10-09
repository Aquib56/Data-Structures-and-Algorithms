class Solution(object):
    def topKFrequent(self, nums, k):
        count,res={},[]
        freq=[[] for i in range(len(nums)+1)]
        print(freq)
        for item in nums:
            count[item]=1+count.get(item,0)
        for key,v in count.items():
            freq[v].append(key)
            
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res