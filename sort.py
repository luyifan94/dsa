def bin_search(array, target):
    start = 0
    end = len(array)
    while(start < end):
        mid = (start+end)//2
        if array[mid] > target:
            end = mid
        elif array[mid] < target:
            start = mid + 1
        else:
            return mid
    return -1

#平均n^2，最好n，最差n^2，辅助空间1
def bubble_sort(array):
    for i in range(len(array)-1):
        flag = True
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                flag = False
        if flag:
            break
    return array

#平均n^2，最好n，最差n^2，辅助空间1，有序时效率高
def insert_sort(array):
    for i in range(1, len(array)):
        insert_key = array[i]
        j = i-1
        while j >= 0 and array[j] > insert_key:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = insert_key
    return array

#平均n^2，最好n^2，最差n^2，辅助空间1
def select_sort(array):
    for i in range(len(array)-1):
        min_key = i
        for j in range(i+1, len(array)):
            if array[j] < array[min_key]:
                min_key = j
        array[i],array[min_key]=array[min_key],array[i]
    return array

#平均nlogn，最好nlogn，最差n^2，辅助空间logn~n
def quick_sort(array):
    quick_sort_sub(array, 0, len(array))
    return array
def quick_sort_sub(array, start, end):
    if end - start <= 1:
        return
    key = start
    for i in range(start + 1, end):
        if array[i] < array[start]:
            key += 1
            array[key], array[i] = array[i], array[key]
    array[start], array[key] = array[key], array[start]

    quick_sort_sub(array, start, key)
    quick_sort_sub(array, key + 1, end)

#平均nlogn，最好nlogn，最差nlogn，辅助空间n
count = 0
def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array)//2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    res = []
    while left and right:
        if left[0] <= right[0]:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))
            global count
            count += len(left)
    res += left or right
    return res

#平均nlogn，最好nlogn，最差nlogn，辅助空间1
def maxheap_adjust(array, start, end):
    child = start * 2 + 1
    while child < end:
        if child + 1 < end and array[child + 1] > array[child]:
            child += 1
        if array[child] > array[start]:
            array[start], array[child] = array[child], array[start]
            start = child
            child = start * 2 + 1
        else:
            break

def maxheap_adjust2(array, start, end):
    child = start * 2 + 1
    if child > end - 1:
        return
    if child + 1 < end and array[child + 1] > array[child]:
        child += 1
    if array[child] > array[start]:
        array[start], array[child] = array[child], array[start]
        maxheap_adjust(array, child, end)

def build_maxheap(array):
    mid = len(array) // 2 - 1;
    for i in range(mid, -1, -1):
        maxheap_adjust(array, i, len(array))

def maxhead_sort(array):
    build_maxheap(array)
    for i in range(len(array) - 1, 0, -1):
        a[0], array[i] = array[i], a[0]
        print(array)
        maxheap_adjust(array, 0, i)

a = [9, 12, 17, 30, 50, 20, 60, 65, 4, 19]
maxhead_sort(a)
print('sorted', a)