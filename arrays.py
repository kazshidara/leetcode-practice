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


