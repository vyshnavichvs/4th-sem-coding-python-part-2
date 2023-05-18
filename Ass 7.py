program to print factorial of the given number without using looping statements                                                                                                   class Solution:

    def factorial(n):

        if n == 0 or n == 1:

            return 1

        else:

            return n * Solution.factorial(n - 1)

# Get user input

num = int(input("Enter a number: "))

# Calculate factorial

solution = Solution()

factorial_result = solution.factorial(num)

print("Factorial of", num, "is:", factorial_result
