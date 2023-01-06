class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        
        count = 0
        for i in costs:
            if coins >= i:
                count += 1
                coins -= i
            else:
                break
        return count