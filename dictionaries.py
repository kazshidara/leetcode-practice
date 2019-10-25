# 1.  K most Frequent values
      
        # :type nums: List[int]
        # :type k: int
        # :rtype: List[int]
 

def topKFrequent(nums, k):
    


    dict = {}
    for i in nums:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
    arr = sorted(dict.items(), key = lambda it: it[1], reverse=True)
    print("sorted by values", arr)
    
    result = []
    for i in range(0,k):
        result.append(arr[i][0])
    return result

print(topKFrequent([1,1,1,2,2,3],2))

################################################################################
