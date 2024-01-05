arr = []

print("Please enter the number array : ", end="")
str = input()
str = str.split()
for item in str:
    arr.append(int(item))

def selectionSort(arr):
    for i in range(len(arr)-1):
        minIndex = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]

selectionSort(arr)
print(arr)