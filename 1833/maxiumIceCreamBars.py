class Solution:
    def maxIceCream(self, costs: list[int], coins: int) -> int:
        costs.sort()
        total = 0
        for c in costs:
            if coins < c:
                break
            coins -= c
            total += 1
        
        return total
    
