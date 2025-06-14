nums = [2, 4, 6, 8, 5, 3, 4, 9]

def asc_selection_sort(arr):
    n = len(arr)

    for i in range(0,n):
        min_ind = i
        # print('i -->', i)
        for j in range(i+1, n):
            # print('arr[min_ind] -->', arr[min_ind])
            # print('arr[j] -->', arr[j])

            if arr[j] < arr[min_ind]:
                min_ind = j
        arr[i], arr[min_ind] = arr[min_ind], arr[i]
    return arr

asc_sort = asc_selection_sort(nums)
print('Ascending sorting', asc_sort)


def dsc_selection_sort(arr):
    n = len(arr)

    for i in range(n):
        max_idx = i 

        for j in range(i+1, n): 
            if arr[j] > arr[max_idx]: 
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i] 
    return arr


dsc_sort = dsc_selection_sort(nums)
print('Descending sorting', dsc_sort)



# OUTPUT
# Ascending sorting [2, 3, 4, 4, 5, 6, 8, 9]
# Descending sorting [9, 8, 6, 5, 4, 4, 3, 2]