def count_subarray_sum_equal_to_k(arr, k):

    count = 0

    curr_sum = 0

    subarray_sum = {0: 1}

    for num in arr:

        curr_sum += num

        count += subarray_sum.get(curr_sum - k, 0)

        subarray_sum[curr_sum] = subarray_sum.get(curr_sum, 0) + 1

    return count

# User input

array = list(map(int, input("Enter the elements of the array, separated by spaces: ").split()))

k = int(input("Enter the value of k: "))

count = count_subarray_sum_equal_to_k(array, k)

print("Count of subarrays with sum equal to", k, ":", count)
