class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [0 for _ in range(amount+1)]
        dp[0] = 1

        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] += dp[i-coin]
                """
                ex) amount = 5, coins = [1, 2, 5] 

                coin :  1  / i :  1  / dp :  [1, 1, 0, 0, 0, 0] -> dp[1] 즉, 1을 만들 수 있는 방법은 1개이다.
                coin :  1  / i :  2  / dp :  [1, 1, 1, 0, 0, 0]
                coin :  1  / i :  3  / dp :  [1, 1, 1, 1, 0, 0]
                coin :  1  / i :  4  / dp :  [1, 1, 1, 1, 1, 0]
                coin :  1  / i :  5  / dp :  [1, 1, 1, 1, 1, 1]
                coin :  2  / i :  2  / dp :  [1, 1, 2, 1, 1, 1] -> dp[2] 즉, 2를 만들 수 있는 방법은 2개이다. = 기존 1로만 만드는 방법 + 2로 만드는 방법 = dp[2-2] = dp[0] + dp[2]
                coin :  2  / i :  3  / dp :  [1, 1, 2, 2, 1, 1]
                coin :  2  / i :  4  / dp :  [1, 1, 2, 2, 3, 1] -> dp[4] 즉, 4를 만들 수 있는 방법은 3개이다. = 기존 1로만 만드는 방법 + 2로 만드는 방법 + 1과 2로 만드는 방법 = dp[2] + dp[4]
                coin :  2  / i :  5  / dp :  [1, 1, 2, 2, 3, 3]
                coin :  5  / i :  5  / dp :  [1, 1, 2, 2, 3, 4]
                """
        return dp[amount]
