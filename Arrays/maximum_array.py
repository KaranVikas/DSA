#given an interger array nums, find the continous subarray(containing at least
# one number) which has the largest sum and return its sum

#example
#Input [-2,-1,-3,4,-1,2,1,-5,4]
#Output 6

#Explanation: [4,-1,2,1] has the largest sum = 6

# the first solution that comes to minc, as always , is the brute force solution
# Here we extract the sum of every possible subarray of the given array and return
# the maximum value.

def brute_force_solution(array):
 maximum = 0
 if len(array) == 0:
     return None
 for i in range(len(array)):
     cum_sum=0
     for j in range(i, len(array)):
         cum_sum += array[j]
         maximum = max(maximum, cum_sum)
 return maximum

array = [-2,1,-3,4,-1,2,1,-5,4]
print(brute_force_solution(array))

