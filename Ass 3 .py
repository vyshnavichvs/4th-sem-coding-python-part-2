def count_subarray_sum_greater_than_k(arr, k):

    count = 0

    curr_sum = 0

    subarray_start = 0

    for subarray_end in range(len(arr)):

        curr_sum += arr[subarray_end]

        while curr_sum <= k:

            curr_sum -= arr[subarray_start]

            subarray_start += 1

        count += len(arr) - subarray_start

    return count

# User input

array = input("Enter the elements of the array, separated by spaces: ").split()

array = [int(num) for num in array]

k = int(input("Enter the value of k: "))

count = count_subarray_sum_greater_than_k(array, k)

print("Count of subarrays with sum greater than", k, ":", count)
