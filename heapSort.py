# 
# 파이썬 힙정렬 알고리즘 
# 시간복잡도 최선: O(nlog2n) 평균: O(nlog2n) 최악: O(nlog2n)

arr = []

# 기본 입력 로직 --------------
print("Please enter the number array : ", end="")
str = input() # 문자열 입력받기
str = str.split() # 공백 기준으로 문자열 자르기
for item in str:
    arr.append(int(item)) # 각각의 요소를 정수형으로 변환후 리스트에 추가
# ----------------------------

# 알고리즘 로직 ---------------
def heapify(arr, index, heap_size):
    largest = index
    left = 2 * index + 1
    right = 2 * index + 2

    if left < heap_size and arr[right] > arr[largest]:
        largest = left
    if right < heap_size and arr[right] > arr[largest]:
        largest = right
    if largest != index:
        arr[largest], arr[index] = arr[index], arr[largest]
        heapify(arr, largest, heap_size)

def heapSort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, i, n)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, 0, i)

    return arr
# ----------------------------

arr = heapSort(arr)
print(arr)