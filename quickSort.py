arr = []

print("Please enter the number array : ", end="")
str = input()
str = str.split()
for item in str:
    arr.append(int(item))

def quickSort(arr) :
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    lower_arr, equal_arr, higer_arr = [], [], []
    for item in arr:
        if item < pivot:
            lower_arr.append(item)
        elif item > pivot:
            higer_arr.append(item)
        elif item == pivot:
            equal_arr.append(item)
    return quickSort(lower_arr) + equal_arr + quickSort(higer_arr)

arr = quickSort(arr)
print(arr)