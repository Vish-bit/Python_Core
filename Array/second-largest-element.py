nums = [55, 32, 97, -55, 45, 32, 88, 21]

def second_largest_element(nums):
    largest = float(-infinity)
    second_largest = nums[0]
    n = len(nums)

    for i in range(0, n):
        largest = max(largest, nums[i])
    print(f"Largest element: {second_largest}")

    for j in range(0, n):
        if (largest > nums[j] > second_largest): 
            second_largest = nums[j] 
    print(f"Second largest element: {second_largest}")
    return
        

second_largest_element(nums)