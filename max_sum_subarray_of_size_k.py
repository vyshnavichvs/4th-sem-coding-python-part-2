class Solution:
    def maximumSumSubarray (self,K,Arr,N):
        # code here
        msum=sum(Arr[0:K])
        csum=msum
        for i in range(K,N):
            csum+=Arr[i]-Arr[i-K]
            msum=max(msum,csum)
        return msum
