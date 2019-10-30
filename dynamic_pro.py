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
        print("initial dp:", dp)
        n = len(coins)
        
        dp[0] = 1
        print(dp)
        for coin in coins:
            for i in range(1, amount + 1):
                if i >= coin:
                    print("i:", i, "A", coin)
                    dp[i] += dp[i - coin]
                print(dp)
        print("final dp:", dp)
        return dp[amount]



# print(change(5,[1,2,5]))

################################################################################