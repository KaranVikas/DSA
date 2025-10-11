#given an array of integers, find if the array contains anu duplicate

#fucntion return true if any value appears at least twice in array, and
# return false if element is distinct

# Input : [1,2,3,1]
#Output: true

#example 2:
# Input: [1,2,3,4]
#Output: false

def brute_force_duplicate_search(array):
    for i in range(len(array)-1):
        for j in range(i+1,len(array)):
            # print(i,j)
            if array[i] == array[j]:
                return True
    return False


array = [1,2,46,32,98,61,34,6]
print(brute_force_duplicate_search(array))

# time complexity - O(n^2)
# a slighlty better solution can be:
# First we sort the array using O(nlogn) built-in sort of Python.
# Then we loop through the array once to check if any consecutive elements
# are same, which will be O(n).
# so overall complexity will be O(nlogn)

def better_duplicate_search(array):
    array.sort()
    for i in range(len(array)-1):
        if array[i] == array[i+1]:
            return True
    return False

array = [1,2,46,32,98,61,34,4]
print(brute_force_duplicate_search(array))

# an even better solution can be using a dictionary.
# As we loop through an array, we'll check first if the current element is
# present in the dictionary
# if yes, we return true
# since looking up in a dictionary is O(1) time, overall complexity would be O(n)

def smart_duplicate_search(array):
    dictionary = dict()
    if len(array)<2:
        return false
    else:
        for i in range(len(array)):
            if array[i] in dictionary:
                return true
            else:
                dictionary[array[i]] = True
        return False

print(smart_duplicate_search(array))
print("smart_duplicate_array")