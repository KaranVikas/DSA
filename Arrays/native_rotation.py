#given an array rotate the array to the right by k steps , where k ins non negatvuve

#example 1:
# Input: nums = [1,2,3,4,5,6,7] , k=3
# Output: [5,6,7,1,2,3,4]

# def naive_rotation(array, k):
#     new_array = []
#     for i in range(k%len(array)):
#         new_array.append(array[len(array)-k+i])
#     for i in range(len(array)-k%len(array)):
#         new_array.append(array[i])
#     return new_array
#
# array = [1,2,3,4,5,6,7,8,9]
# k=11
# print(naive_rotation(array,k))


#  A better solutiom can be using the Reversal Algorithm
# in this, we first reverse the entire array, then we reverse the first k elements,
# followed by reversing the last n-k elements
# since, the time complexity of reversing is O(n)
#therefore, overall time complexity for this Algorithm would be O(3n)
# which is equal to O(n), with no extra space required


def reverse(array, start, end):
    while start<end:
        print(start,end)
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1
    return array

def reverse_rotate(array, k):
    array = reverse(array,0,len(array)-1)
    print(array)
    array = reverse(array,0,k%len(array)-1)
    print(array)
    array = reverse(array,k%len(array), len(array)-1)
    print(array)

a = [1,2,3,4,5,6,7,8,9]
k = 11 
print(reverse_rotate(a,k))