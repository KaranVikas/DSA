
# Given an array nums, write a function to move all 0's to the end of it while
# maintaining its relative order of the non-zeros'
# example
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]

# The first solution that comes to mind is we can traverse the original length
# of the array and for every zero we find
# we append a 0 at the end of the array, for the original length of the array
# and we pop every 0 that we find, thus removing every 0 from the original part of \
# the array and moving them all to the end.
# This seems inefficent as pop operation anywhere apart from the end of the array
# cost O(n) time
# and we have loop over the entire array so it becomes O(n^2), but lets see


def naive_zero_mover(array):
    l = len(array)
    for i in range(l):
        if array[i] == 0:
            array.append(0)
    #         now we have append 0's at the end for every 0 in the original array
    j=0
    c=0
    while(c < l):
        # looping the array for 1 times i.e, the original length of the array
        if(array[j]!=0):
            j+=1
        # if the element is non-zero we increment j by 1 ,which keeps track of
        # every index of the array upto 1
        else:
            array.pop(j)
        c += 1
    return array

array = [0,0,0,0,1,0,3,0,0,0,12,9,7]
print(naive_zero_mover(array))

# a far better solution can be swapping every non-zero element we find with the first
# un-swapped zero

def swap_move(array):
    z=0
    for i in range(len(array)):
        if array[i]!=0:
            array[i],array[z]=array[z],array[i]
            z += 1
    return array
print(swap_move(array))

