import math
class Solution:
    def checkStraightLine(self, coord: List[List[int]]) -> bool:
        coord = sorted(coord)
        x = []
        for i in range(len(coord)-1):
            if((coord[i][0] - coord[i+1][0])==0):
                if((coord[i][1] - coord[i+1][1])>0):
                    x.append(math.atan(float("inf")))
                elif((coord[i][1] - coord[i+1][1])<0):
                    x.append(math.atan(float("-inf")))
            else:
                x.append(math.atan((coord[i][1] - coord[i+1][1])/(coord[i][0] - coord[i+1][0])))
        return True if(len(set(x))== 1) else False