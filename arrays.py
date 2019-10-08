# 1.  Intersection of 2 arrays


def intersect(nums1, nums2):
    """ Given two arrays, write a function to compute their intersection. """
    
    set1 = set(nums1)
    set2 = set(nums2)
    intersect = set1 & set2
    return list(intersect)

################################################################################


#  2. Given an array of integers, find if the array contains any duplicates.

        # Your function should return true if any value appears at least twice 
        # in the array, and it should return false if every element is distinct.

def find_duplicates(nums):

    set1 = set(nums)
    if len(set1) < len(nums):
        return True
    elif len(set1) == len(nums):
        return False 


################################################################################


#  3. Single Number 

# Given a non-empty array of integers, every element appears twice except for one. 
# Find that single one. Your algorithm should have a linear runtime complexity. 
# Could you implement it without using extra memory?

def find_single(nums):

    num_dict = {}
    for num in nums:
        num_dict[num] = num_dict.get(num, 0) + 1
    for key, value in num_dict.items():
        if value == 1:
            return key

################################################################################


#  4. Move Zeroes to end of the array 

# Given a non-empty array of integers, write fcn to move all 0's to end of array 
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.

def move_zeros(nums):

    zeros = []
    non = []
        
    for num in nums:
        if num == 0:
            zeros.append(0)
        else:
            non.append(num)
    return non + zeros

#  To change the list in place, use pointers!!

def move_zeros(nums):

    zero = 0

    for i, num in enumerate(nums):
        if num != 0:
            nums[i], nums[zero] = nums[zero], nums[i]
            zero += 1


################################################################################


# 5. Majority Element

# Given an array of size n, find the majority element. The majority element 
# is the element that appears more than ⌊ n/2 ⌋ times.

def get_majority(nums):

    new_dict = {}

    for num in nums:
        new_dict[num] = new_dict.get(num, 0) + 1
    for key, value in new_dict.items():
        if value > (len(nums)/2):
            return key

################################################################################

# 6. Find all NUmbers Disappeared 

# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

# Find all the elements of [1, n] inclusive that do not appear in this array.

# Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

def findDisappearedNumbers(nums):
    dict = {}
    list = []
    for i in range(min(nums), max(nums)+1):
        dict[i] = dict.get(i, 0)
    for num in nums:
        dict[num] = dict.get(num, 0) + 1
    
    for key, value in dict.items():
        if value == 0:
            list.append(key)
    return list

# FOR BETTER SPACE COMPLEXITY:::

def fcn(nums):

    for i in range(len(nums)):
        index = abs(nums[i]) - 1
        nums[index] = - abs(nums[index])

    return [i + 1 for i in range(len(nums)) if nums[i] > 0]

################################################################################




