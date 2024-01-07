# 
# 파이썬 선택정렬 알고리즘 
# 시간복잡도 최선: O(n^2) 평균: O(n^2) 최악: O(n^2)

arr = []

# 기본 입력 로직 --------------
print("Please enter the number array : ", end="")
str = input() # 문자열 입력받기
str = str.split() # 공백 기준으로 문자열 자르기
for item in str:
    arr.append(int(item)) # 각각의 요소를 정수형으로 변환후 리스트에 추가
# ----------------------------

# 알고리즘 로직 ---------------
def selectionSort(arr):
    for i in range(len(arr)-1): # arr의 길이 - 1 만큼 반복 (이유 아래 후술)
        minIndex = i # 최솟값 인덱스 초기화
        for j in range(i+1, len(arr)): # i+1 부터 arr길이 만큼 반복
            if arr[j] < arr[minIndex]: 
                # arr[i]를 arr[i+1]부터 arr[len(arr)] 까지 비교하여 더 작은 값이 있다면
                minIndex = j # 최솟값의 인덱스를 변경하고
        arr[i], arr[minIndex] = arr[minIndex], arr[i] # 최솟값을 리스트의 가장 앞으로 이동
# ----------------------------

# for i 가 len(arr)-1 만큼만 반복하는 이유
# 같은 값을 비교할 필요가 없기 때문
# i = len(arr) 이고 j = len(arr)일때 arr[i] = arr[j] 이므로 값을 비교할 필요가 없기 때문
# for j문이 i+1 부터 시작하는 것도 같은 이유


selectionSort(arr)
print(arr)