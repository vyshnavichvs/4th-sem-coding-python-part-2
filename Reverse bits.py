class Solution:

    def reverseBits(self, n: int) -> int:

        res=0

        for i in range(0,31):

            if (n&1)==1:

                res=res+1

            n=n>>1

            res=res<<1

        return res+(n&1)
