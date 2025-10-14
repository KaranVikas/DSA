# first approach , take an array and append the string element in the reverse order


# A smarter way to do this, can be taking a pair of elements
# from either end of the string and swapping them
# we have start at both the ends and continue swapping parts till
# the middle of string
# This way we can avoid having to create a new array and save on space complexity
#  while keeping time complexity at O(n)

string = "karan"
def swap(string, a , b):
    print(string)
    string = list(string)
    print(string)
    temp = string[a]
    string[a] = string[b]
    string[b] = temp
    return ''.join(string)

def smart_reverse(string):
    for i in range(len(string)//2):
        string = swap(string, i , len(string)-i-1)
    return string

print(smart_reverse(string))