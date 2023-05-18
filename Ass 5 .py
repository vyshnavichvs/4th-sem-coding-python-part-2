def count_max_subarray_product(arr, k):

    count = 0

    for i in range(len(arr)):

        product = 1

        for j in range(i, len(arr)):

            product *= arr[j]

            if product <= k:

                count += 1

            else:

                break

    return count

array = list(map(int, input("Enter the array elements separated by space: ").split()))

k = int(input("Enter the value of k: "))

result = count_max_subarray_product(array, k)

print("Count of maximum subarray product <= k:", result)
