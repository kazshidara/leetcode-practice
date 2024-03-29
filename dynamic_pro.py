# Coin Change 2 

# Given an array of different coin values and total amount these values should
# add up to, return total number of combinations

# Idea: Inspect each coin and for each coin, see how many different way it can 
# go into a range from 1-amount specified
#  Use array to keep track and return the value of array at amount.--> dp[amount]



def change(amount, coins) -> int:
        if amount == 0:
            return 1
        if not coins:
            return 0
        
        dp = [0] * (amount + 1)
       
        n = len(coins)
        
        dp[0] = 1

        for coin in coins:
            for i in range(1, amount + 1):
                if i >= coin:
                    dp[i] += dp[i - coin]
        return dp[amount]



# print(change(5,[1,2,5]))

################################################################################

# Letter combinations of a phone number (phone number --> letter)


def letterCombinations(digits):
    letters = { '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                                 '6': 'mno', '7': 'pqrs', '8': 'tuv', '9':'wxyz' }       
    result = []

    def helper(digits, comb=""):

        if digits == "":
            if comb != "":
                result.append(comb)
                print(result)

        else:

            for letter in letters[digits[0]]:

                helper(digits[1:], comb+letter)
    helper(digits)
    return result


# print(letterCombinations("23"))


################################################################################


# Maximum squares in a 2D array 

def find_max_squares(matrix):

    if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):

            if len(matrix) == 1 and len(matrix[0]) == 1 and matrix[0][0] == 1:
                return 1

            elif len(matrix) == 1 and len(matrix[0]) == 1 and matrix[0][0] == 0:
                return 0

    result = 0
    squares = matrix.copy()
    
    for row in range(len(squares)):
        for column in range(len(squares[row])):
            if row == 0 or column == 0:
                continue 
            elif int(squares[row][column]) > 0:
                squares[row][column] = 1 + min(int(squares[row-1][column]),int(squares[row][column-1]), int(squares[row-1][column-1]))
            if int(squares[row][column]) > result:
                result = int(squares[row][column])
    return result*result 
    

# print(find_max_squares([[1]]))
# print(find_max_squares([[0]]))

################################################################################

#Product of 2 strings 
# not really DP but cool trick to write out alg. that multiplies 2 number strings together

def multiply(num1:str, num2:str):

    result = 0
    carry1 = 1
    for n1 in num1[::-1]:
        carry2 = 1
        for n2 in num2[::-1]:
            result += int(n1)*int(n2)*carry1*carry2
            carry2 *= 10
        carry1 *= 10
    return str(result)

# print(multiply("123","456"))

