class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        d=[]
        non=[]
        for i in range (n+1):
            if i%m==0:
                d.append(i)
            else:
                non.append(i)
        return sum(non)-sum(d)
        


                   
