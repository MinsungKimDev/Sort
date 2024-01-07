# 
# 파이썬 퀵정렬 알고리즘 
# 시간복잡도 최선: O(nlog2n) 평균: O(nlog2n) 최악: O(n^2)

arr = []

# 기본 입력 로직 --------------
print("Please enter the number array : ", end="")
str = input() # 문자열 입력받기
str = str.split() # 공백 기준으로 문자열 자르기
for item in str:
    arr.append(int(item)) # 각각의 요소를 정수형으로 변환후 리스트에 추가
# ----------------------------

# 알고리즘 로직 ---------------
def quickSort(arr) :
    if len(arr) <= 1: # 리스트의 길이가 1보다 작거나 같으면 
        return arr # 리스트 자체를 리턴(정렬할 필요가 없음)
    
    pivot = arr[len(arr) // 2] # 리스트의 중간값을 피벗으로 설정
    lower_arr, equal_arr, higer_arr = [], [], [] # 피벗보다 작은 리스트, 같은 리스트, 큰 리스트를 각각 생성

    for item in arr: 
        if item < pivot: # 리스트의 아이템이 피벗보다 작으면
            lower_arr.append(item) # lower_arr에 추가
        elif item > pivot: # 리스트의 아이템이 피벗보다 크면
            higer_arr.append(item) # higer_arr에 추가
        elif item == pivot: # 리스트의 아이템이 피벗과 같으면
            equal_arr.append(item) # equal_arr에 추가
    return quickSort(lower_arr) + equal_arr + quickSort(higer_arr) # 피벗 좌, 우의 리스트는 같은방법으로 계속 정렬
# ----------------------------

arr = quickSort(arr)
print(arr)