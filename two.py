arr = input("Enter the array: ")
arr = [int(x) for x in arr.split()]
m = len(arr)
n = m + 1


def find_missing_number(nums, n):
    total_sum = (n * (n + 1)) // 2
    remaining_sum = sum(nums)
    missing_number = total_sum - remaining_sum
    return missing_number


print(find_missing_number(arr, n))

#O(N)
