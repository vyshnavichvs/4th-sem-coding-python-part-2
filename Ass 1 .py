def max_subarray_sum(arr):

    max_sum = float('-inf')

    curr_sum = 0

    

    for num in arr:

        curr_sum += num

        if curr_sum > max_sum:

            max_sum = curr_sum

        if curr_sum < 0:

            curr_sum = 0

    

    return max_sum

array = input("Enter the elements of the array, separated by spaces: ").split()

array = [int(num) for num in array]

max_sum = max_subarray_sum(array)

print("Maximum subarray sum:", max_sum)
