# 가장 작은 것을 선택해 맨 앞에 있는 데이터와 바꾸고
# 그 다음 가장 작은 데이터를 선택해 앞에서 두 번째 데이터와 바꾸는 과정을 반복하는 알고리즘
# 시간복잡도는 O(N^2)으로 비효율적이지만 특정 리스트에서 가장 작은 데이터를 찾는 일이 종종 있으므로 알아둘 것!
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i # 가장 작은 원소의 인덱스
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j] :
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] # swap

print(array) 
