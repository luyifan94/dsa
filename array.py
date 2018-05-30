def union_interval(array):
    array.sort()
    temp = res = list(array[0])
    for i in range(1,len(array)):
        if array[i-1][1] > array[i][0] and array[i-1][1] < array[i][1]:
            temp[1] = array[i][1]
        else:
            temp = list(array[i])
        if temp[1]-temp[0] > res[1] - res[0]:
            res = temp
    return tuple(res)

array = [(2,4),(3,6),(1,3),(6,7)]
print(union_interval(array))
#test