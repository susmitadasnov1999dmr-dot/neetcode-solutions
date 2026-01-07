class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        nums=list(order)
        nums2=list(friends)
        nums3=[]
        for i in  nums:
            
            for j in  nums2:
                if j==i:
                    nums3.append(i)
        return nums3
        
