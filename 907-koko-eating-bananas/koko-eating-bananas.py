class Solution:
    def minEatingSpeed(self, piles, h):
        left = 1
        right = max(piles)

        while left < right:
            mid = (left + right) // 2

            if self.canEat(piles, h, mid):
                right = mid
            else:
                left = mid + 1

        return left

    def canEat(self, piles, h, speed):
        hours = 0

        for pile in piles:
            hours += (pile + speed - 1) // speed

        return hours <= h