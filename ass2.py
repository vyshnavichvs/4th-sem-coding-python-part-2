class Solution:
    def reverseString(self, s: List[str]) -> None:
        n=len(s)
        for i in range(0,n//2):
            s[i],s[-i-1]=s[-i-1],s[i]

        return s
