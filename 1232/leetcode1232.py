from typing import List
class Solution:
    def checkStraightLine(self, coords: List[List[int]]) -> bool:
        if len(set(x for x, y in coords)) == 1: return True 
        if len(set(x for x, y in coords)) < len(coords): return False
        return len(set((p1[1] - p2[1])/(p1[0] - p2[0]) for p1, p2 in zip(coords, coords[1:]))) == 1
