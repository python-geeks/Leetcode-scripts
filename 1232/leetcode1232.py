class Solution:
    def checkStraightLine(self, A: List[List[int]]) -> bool:
        results = []
        for i in A:
            for j in A:
                try:
                    results.append(
                        (i[1]-j[1]) / (i[0]-j[0])
                    )
                except:
                    pass
        return all([
            i == results[0]
            for i in results
        ])
