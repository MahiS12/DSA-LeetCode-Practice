class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        list1=[]
        for i in nums:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
        index= sorted(count.values(),reverse=True)[k-1]
        for i in count:
            if count[i] <index: continue
            else: list1.append(i)
        return list1