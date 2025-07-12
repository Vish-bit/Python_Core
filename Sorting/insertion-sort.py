## Insertion Sorting

nums = [9, 15, 11, 2, 8, 10, 5]

def insertion_sort(nums):
    n = len(nums)
    for i in range(1, n):
        key = nums[i]
        j = i-1

        while j>=0 and nums[j] > key:
            nums[j+1] = nums[j]
            j-=1
        nums[j+1] = key
    print("Sorted -> ", nums)
    return 

insertion_sort(nums)
