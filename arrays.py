# 1.  Intersection of 2 arrays


def intersect(nums1, nums2):
""" Given two arrays, write a function to compute their intersection. """
    
    set1 = set(nums1)
    set2 = set(nums2)
    intersect = set1 & set2
    return list(intersect)

################################################################################


