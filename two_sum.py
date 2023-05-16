class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr=sorted(nums)
        n=len(nums)
        res=[]
        if n==1:
            return nums
        l=0
        r=n-1
        while(l<r):
            if arr[l]+arr[r]==target:
                break
            elif arr[l]+arr[r]>target:
                r=r-1
            else:
                l=l+1
        for i in range(n):
            if nums[i]==arr[l]:
                res.append(i)
            elif nums[i]==arr[r]:
                res.append(i)
        return res
