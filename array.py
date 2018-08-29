def union_interval(array):
    array.sort()
    temp = res = list(array[0])
    for i in range(1,len(array)):
        if array[i-1][1] > array[i][0] and array[i-1][1] < array[i][1]:
            temp[1] = array[i][1]
        else:
            temp = list(array[i])
        if temp[1]-temp[0] > res[1]-res[0]:
            res = temp
    return tuple(res)

array = [(2,4),(3,6),(1,3),(6,7)]
print(union_interval(array))
#test

def binary_search(array, target):
    left = 0
    right = len(array)-1
    while(left < right):
        mid = (left+right)//2
        if array[mid] > target:
            right = mid
        elif array[mid] < target:
            left = mid + 1
        else:
            return mid
    return left
def longest_increasing_subsequence(arr):
    n = len(arr)
    sub = [1]*n
    for i in range(n):
        tmax = 1
        for j in range(i):
            if arr[j] < arr[i]:
                tmax = max(tmax, sub[j]+1)
        sub[i] = tmax
    return sub
def longest_increasing_subsequence2(arr):
    n = len(arr)
    lst = [arr[0]]
    for i in range(1, n):
        if arr[i] > arr[i-1]:
            lst.append(arr[i])
        else:
            # 这部可以改为二分查找使复杂度降为nlogn
            # t = binary_search(lst, arr[i])
            # lst[t] = arr[i]
            for j in range(len(lst)):
                if lst[j] > arr[i]:
                    lst[j] = arr[i]
                    break
    return len(lst)