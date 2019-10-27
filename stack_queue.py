# 1.  Implement a Queue using Stacks


class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.inStack = []
        self.outStack = []
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.inStack.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
        return self.outStack.pop()
        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
        return self.outStack[-1]
         

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if (not self.inStack) and (not self.outStack):
            return True 
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

################################################################################

# 2.  Balanced Brackets  (HACKERRANK)

# Complete the function isBalanced in the editor below. 
# It must return a string: YES if the sequence is balanced or NO if it is not.


def is_balanced(s):
    stack = []
    d = {'}':'{',
         ']': '[',
         ')': '('
    }

    for char in s:
        if char in d.values():
            stack.append(char)
        elif char in d.keys():
            if stack == [] or d[char] != stack.pop():
                return "NO"
        else:
            return "NO"


    if stack == []:
        return "YES"
    else:
        return "NO"

################################################################################

# 3.  Game of 2 Stacks! (HACKERRANK)

# 14. Maximum Subarray Sum (HACKERRANK)

def twoStacks(x, a, b):
    
    sum_ints = 0
    num_ints = 0
    pa = 0
    pb = 0

    while sum_ints <= x and (pa <=len(a) or pb <= len(b)):

        popped = min(a[pa], b[pb])
        print("popped value", popped)

        if (sum_ints + popped) > x:
            return num_ints

        sum_ints += popped
        print("sum of ints", sum_ints)

        num_ints += 1
        print("num of ints", num_ints)

        if popped == a[pa]:
            pa += 1
        if popped == b[pb]:
            pb += 1

    return num_ints


print(twoStacks(10, [4,2,4,6,1],[2,1,8,5]))
