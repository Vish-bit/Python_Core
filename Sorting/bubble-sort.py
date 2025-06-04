def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        is_swap = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]: 
                arr[j], arr[j + 1] = arr[j + 1], arr[j] 
                is_swap = True
        if is_swap == False:
            print('No sorting required')
            print('Sorted Array - ', arr)
            break



nums1 = [5, 4, 7, 9, 0, 6, 1, 2]
nums2 = [1,3,4,6,7,9,12,45]
bubble_sort(nums1)
bubble_sort(nums2)