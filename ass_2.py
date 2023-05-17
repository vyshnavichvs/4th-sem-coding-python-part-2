def minSum (arr, n) : 

        for i in range(1,n):

            if arr[i]<=arr[i-1]:

                arr[i]=arr[i-1]+1

        return sum(arr)
