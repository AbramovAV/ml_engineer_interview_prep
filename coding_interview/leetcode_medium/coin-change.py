class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins_array = [amount+1] * (amount+1)
        coins_array[0] = 0
        for i in range(amount+1):
            for coin in coins:
                if coin <= i:
                    coins_array[i] = min(coins_array[i], coins_array[i-coin]+1)

        if coins_array[amount] == amount + 1:
            return -1
        else:
            return coins_array[amount]