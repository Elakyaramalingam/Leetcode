class Solution:
    def shipWithinDays(self, weights, days):
        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = (left + right) // 2

            if self.canShip(weights, days, mid):
                right = mid
            else:
                left = mid + 1

        return left

    def canShip(self, weights, days, capacity):
        days_needed = 1
        current_weight = 0

        for weight in weights:
            if current_weight + weight > capacity:
                days_needed += 1
                current_weight = 0

            current_weight += weight

        return days_needed <= days
        