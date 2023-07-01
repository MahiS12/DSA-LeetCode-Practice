class Solution(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        s=[]

        for i in range(1,n//2+1):
            if n%i==0:
                s.append(i)

        s.append(n)
        if k > len(s):
            return -1
        return s[k-1]


        # for i in range(1, n+1):
        #     if n%i ==0:
        #         k-=1
        #         if k ==0:
        #             return i
        # return -1
