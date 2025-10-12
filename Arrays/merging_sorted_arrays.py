# given 2 sorted arrays , we need to merge them and create
# one big sorted array.

# for example, array = [1,3,5,7], array2 = [2,4,6,8]

def merge(array1, array2):
    new_array = []
    flag = 0
    first_array_index  = second_array_index = 0
    while not(first_array_index >= len(array1)  or second_array_index >= len(array2)):
        if array1[first_array_index] <= array2[second_array_index]:
            new_array.append(array1[first_array_index])
            first_array_index += 1
            print(first_array_index)

        else:
            new_array.append(array2[second_array_index])
            second_array_index += 1

        if first_array_index == len(array1):
            flag = 1

    if flag == 1:
        for item in array2[second_array_index:]:
            new_array.append(item)

    else:
        for item in array1[first_array_index:]:
            new_array.append(item)

    return new_array

array1 = [1,3,5,7]
array2 = [2,4,6,8,10,12]
print(merge(array1,array2))

