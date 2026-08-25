#1 write a python program to find the longest consecutive increasing sequence in tuple and display its element
#input:(3,5,7,2,4,5,6,8,1,9)
#output(2,4,6,8)
"""
t = (3, 5, 7, 2, 4, 5, 6, 8, 1, 9)

longest = ()
current = [t[0]]

for i in range(1, len(t)):
    if t[i] > t[i - 1]:
        current.append(t[i])
    else:
        if len(current) > len(longest):
            longest = tuple(current)
        current = [t[i]]

if len(current) > len(longest):
    longest = tuple(current)

    
print(longest)

"""
#2 List — Find the contiguous subarray with maximum sum.
"""nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

current = nums[0]
maximum = nums[0]

for i in range(1, len(nums)):
    current = max(nums[i], current + nums[i])
    maximum = max(maximum, current)

print(maximum)"""

#3 Sets — Find elements occurring in exactly one of two sets.
A={10,20,30,40,50}
B={30,40,60,70}
res= A.symmetric_difference(B)
print(res)
