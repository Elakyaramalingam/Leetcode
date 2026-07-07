class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        for i in range(1,20):
            if n*i%2==0:
                m=n*i
                break
        return m
        