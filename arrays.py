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

# 6. Find all Numbers Disappeared 

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

#  7. TWO SUM

# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

def two_sum(nums, target):

    # add the numbers in the dictionary as you iterate through the numbers  
    num_dict = {}

    for i, num in enumerate(nums):
        m = target - num
        if m in num_dict:
            return [num_dict[m], i]
        else:
            num_dict[num] = i


################################################################################

#  8. MAXIMUM SUBARRAY

# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Example:

# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6

def max_subarray(nums):

    max_sum = max(nums)
    curr_sum = 0

    for num in nums:
        curr_sum += num
        max_sum = max(max_sum, curr_sum)

        if curr_sum < 0:
            curr_sum = 0
    return max_sum


################################################################################

#  9. Minimum Index Sum of Two Lists

# Suppose Andy and Doris want to choose a restaurant for dinner, and they both have 
# a list of favorite restaurants represented by strings. You need to help them find 
# out their common interest with the least list index sum. If there is a choice tie
#  between answers, output all of them with no order requirement. You could assume 
#  there always exists an answer.

def findRestaurant(list1, list2):
    """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
    """
        
    set1 = set(list1)
    set2 = set(list2)
    same_set = set1 & set2
    
    if not same_set:
        return []
    elif len(same_set) == 1:
        return list(same_set)
    elif len(same_set) > 1:
        same_dict = {}
        for i1,res1 in enumerate(list1):
            if res1 in same_set:
                same_dict[res1] = same_dict.get(res1, 0) + i1
        for i2, res2 in enumerate(list2):
            if res2 in same_set:
                same_dict[res2] += i2
        min_value = min(same_dict.values())
        print(min_value)
        return [key for key in same_dict.keys() if same_dict[key] == min_value]


        # for i2,res2 in enumerate(list2):



# print(findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"],["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]))
# print(findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"],["KFC", "Shogun", "Burger King"]))

################################################################################

# 10. New Year Chaos, number of swaps to get to sorted array 

# Given an array of intergers, determine number swaps that it took to get array 
# to sorted order
#     --> 1 element cannot swap more than 2 times, if it does print "Too Chaotic"
    

def minimumBribes(q):

    swaps = 0
    d = {}

    p1 = 0
    p2 =1

    while q != q.sort():

        if q[p1] < q[p2]:
            p1 += 1
            p2 += 2

        elif q[p1] > q[p2]:
            swaps += 1
            d.get(q[p1],0) + 1
            print("Dictionaryyyy",d)
            q[p1],q[p2] = q[p2],q[p1]
            p1 += 1
            p2 += 1
        if p2 == len(q)-1:
            p1 = 0
            p2 = 1
    for value in d.values():
        if value > 2:
            return "Too Chaotic"
        else:
            return swaps




minimumBribes([2,5,1,3,4])
