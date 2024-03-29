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
    pass





################################################################################

# 11. Compare strings by freq of smallest character 



################################################################################

# 12. Product of Array except Self 

# Given an array nums of n integers where n > 1,  
# return an array output such that output[i] is equal to the product of all
#  the elements of nums except nums[i].

# Test Case:  Input:  [1,2,3,4]
#             Output: [24,12,8,6]

def product_except_self(nums):

    result = [1]*len(nums)
    
    product_left = 1
    for i in range(1, len(nums)):
        product_left *= nums[i-1]
        result[i] *= product_left

    product_right = 1
    for i in range(len(nums)-2, -1,-1):
        product_right = product_right * nums[i+1]
        result[i] *= product_right 
    return result


# print(product_except_self([1,2,3,4]))

################################################################################

# 13. Top K frequent words



def top_freq_words(words, k):
    _dict = {}
    result = []
        
    for word in words:
        if word in _dict:
            _dict[word] += 1
        else:
            _dict[word] = 1

    sorted_dict = Counter(_dict)
    print(sorted_dict)
    

    array = sorted(_dict.items(), key=lambda x:x[1], reverse=True)

    

    for i in range(0,k):
        result.append(array[i][0])
    print(result)
    


# print(top_freq_words(["i", "love", "leetcode", "i", "love", "coding"], 3))
    

################################################################################


# 14. Maximum Sub Array 

def max_subarray(arr, m):
    best = 0
    mod_vals = [x % m for x in arr]
    print("array:", arr)
    print("mod_vals:", mod_vals)
    running_totals = []

    for i in range(len(mod_vals)):
        if mod_vals[i] == m-1:
            best = m-1
            return best
        if i > 0:
            running_totals.append((mod_vals[i]+running_totals[i-1]) % m)
            print("Running_totals:", running_totals)
        else:
            running_totals.append(mod_vals[i])
            print("Running_totals:", running_totals)
    print("Running_totals:", running_totals)

    sorted_partials = sorted(running_totals)
    print("sorted partials= sorted running totals:", sorted_partials)

    position = {}
    for i, x in enumerate(running_totals):
        if x not in position:
            position[x] = i
    print("position dict:", position)

    for i in range(1,len(sorted_partials)):
        if best == m-1:
            break

        a, b = sorted_partials[i], sorted_partials[i-1]
        print("a:", a)
        print("b:", b)
        best = max(best, a)
        print("best", best)
        if position[a] < position[b] and a != b:
            best = max(best, (b-a) % m)
            print("best", best)


    return best


# print(max_subarray([3,3,9,9,5],7))


################################################################################


# 15. Brick Wall
import collections

def leastBricks(wall):
        
    d=collections.defaultdict(int)
    for w in wall:
        cur=0
        for v in w:     
            cur+=v
            d[cur]+=1
        d[cur]-=1
        print("final d:",d)
    return len(wall)-max(d.values())

# print(leastBricks([[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]))


################################################################################


# 16. Merge Intervals

def merge(intervals):

    merged_list = []

    for interval in intervals:

        if not merged_list:
            merged_list.append(intervals[0])

        elif merged_list[-1][-1] < interval[0]:
            merged_list.append(interval)

        else:
            merged_list[-1][-1] = max(merged_list[-1][-1], interval[0])

    return merged_list



# print(merge([[1,3],[2,6],[8,10],[15,18]]))


# print(merge([[1,4],[4,5]]))

################################################################################


# 17. Meeting Rooms 
    

# def minMeetingRooms(intervals):

#     counter = len(intervals)
#     end_times = [interval[1] for interval in intervals]

#     for interval in intervals:
#         for time in end_times:
#             if interval[0] >= endtime:
#                 counter -= 1
#             elif interval

    

################################################################################


# 18. Num Islands 


def dfs(grid,i,j):

    if i<0 or i>=len(grid) or j<0 or j>=len(grid[i]) or grid[i][j] == '0':
        return 0

    grid[i][j] == '0'

    dfs(grid,i+1,j)
    dfs(grid,i-1,j)
    dfs(grid,i,j+1)
    dfs(grid,i,j-1)

    return 1

def number_islands(grid):

    counter = 0

    if len(grid) == 0 or grid == None:
        return 0

    for i in range(0,len(grid)):
        for j in range(0,len(grid[i])):
            if grid[i][j] == 1:
                counter += dfs(grid,i,j)
        return counter 


# print(number_islands([[1,1,1,1,0],
#                       [1,1,0,1,0],
#                       [1,1,0,0,0],
#                       [0,0,0,0,0]]))

################################################################################


# 19. Sub array Sum equals K

# Given an array of integers and an integer k, you need to find the total number 
# of continuous subarrays whose sum equals to k.

# Input:nums = [1,1,1], k = 2
# Output: 2




def subarray_sum(nums, k):

    current_sum = 0
    counter = 0
    nums.sort()
    p1 = 0
    p2 = 1

    while p2 < len(nums):
        current_sum += (nums[p1]+nums[p2])
        print(current_sum)
        if current_sum < k:
            p2+=1
            print(p1,p2)
        elif current_sum == k:
            counter += 1
            p1 = p2
            p2+=1
            current_sum = 0
            print(p1,p2)
        else:
            break

    return counter 


# print(subarray_sum([1,2,3],3))



################################################################################

# 20. Recursion problem from Corey 

# Given an array of integers and an integer k, you need to return True if array 
# can be split into 'k' subarrays and each subarray having same sum

# Input:nums = [1,3,2], k = 2
# Output: [1,2],[3] -- True 

def helper(nums, result_array, target_sum, k):



    if result_array == ([target_sum]*k):
        return True 


    for group in result_array:
        print(group)
        temp = group + nums[0]
        print(temp)

        if temp > target_sum:
            continue 
        elif temp <= target_sum:
            result_array = result_array[group] + nums[0]
            helper(nums[1:], result_array, target_sum,k)


################################################################################

# 21. 


def k_subarrays(nums, k):

    if sum(nums) % k != 0:
        return False 

    target_sum = (sum(nums))/k
    result_array = [0] * k
    print(result_array)

    helper(nums, result_array, target_sum, k)



# print(k_subarrays([1,3,2],2))



################################################################################

# 22. Search in rotated sorted array 

def binary_search(nums, target):

    left = 0
    right = len(nums) - 1

    while left < right: 
        mid = int((left + right)/2)
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid


    start = left
    left = 0
    right = len(nums) - 1

    if (target >= nums[start]) and (target <= nums[right]):
        left = start 
    else:
        right = start

# implement binary search by setting midpoint:
    while left <= right:
        middle = int((left + right)/2)

        if nums[middle] == target:
            return middle
        elif nums[middle] > target:
            right = middle 
        else:
            left = middle + 1

    return -1 


# print(binary_search([4,5,6,7,0,1,2], 5))


################################################################################

# 23. Compare Strings by Frequency of the Smallest Character

def count_smallest_char(word):
    count = 0
    smallest = min(word)

    for char in word: 
        if char == smallest:
            count += 1
    return count 











