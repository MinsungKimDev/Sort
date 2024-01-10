arr = []

# 기본 입력 로직 --------------
print("Please enter the number array : ", end="")
str = input() # 문자열 입력받기
str = str.split() # 공백 기준으로 문자열 자르기
for item in str:
    arr.append(int(item)) # 각각의 요소를 정수형으로 변환후 리스트에 추가
# ----------------------------

# 알고리즘 로직 ---------------
def bubbleSort(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
# ----------------------------
                
arr = bubbleSort(arr)
print(arr)