arr = [1,2,5,6,8,0,12]
i = 0

while i < len(arr):
    if arr[i] % 2 == 0:
        arr.insert(i + 1, arr[i])
        i += 2
    else:
        i += 1
print('Arr List', arr)
    


