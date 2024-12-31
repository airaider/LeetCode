class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        dp = [0] * (days[-1] + 1)

        travel_days = set(days)

        for day in range(1, days[-1] + 1):
            if day not in travel_days:
                dp[day] = dp[day - 1]
            else:
                dp[day] = min(
                    dp[day - 1] + costs[0],
                    dp[max(0, day - 7)] + costs[1],
                    dp[max(0, day - 30)] + costs[2]
                )

        return dp[days[-1]]