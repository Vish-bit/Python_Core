nums = [55, 32, -97, 99, 3, 67]

def largest_element(nums):
    largest = nums[0]
    n = len(nums)

    for i in range(0, n):
        largest = max(largest, nums[i])
    print(f"Largest element: {largest}")
    return largest

largest_element(nums)
