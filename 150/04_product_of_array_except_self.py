from typing import List

class Solution:
    def productExceptSelf(selfself, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= postfix
            postfix *= nums[i]
            print(i, res[i], postfix)
        return res

nums = 1,2,3,4

sol = Solution()
print(sol.productExceptSelf(nums))


# nums = [1,2,3,4]
# res = [1]*(len(nums))
# print(res)
# prefix = 1
# for i in range(len(nums)):
#     res[i] = prefix
#     prefix *= nums[i]
#     print(i, res[i], prefix)
# postfix = 1
# print(res)
# for i in range(len(nums)-1,-1,-1):
#     res[i] *= postfix
#     postfix *= nums[i]
#     print(i, res[i], postfix)
# # return res
# print(res)
