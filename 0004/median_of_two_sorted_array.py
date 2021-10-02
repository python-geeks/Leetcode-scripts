class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        x = len(nums1)
        y = len(nums2)
        if y < x:
            # Making sure nums1 is the smaller length array
            return self.findMedianSortedArrays(nums2, nums1)

        maxV = float('inf')
        minV = float('-inf')
        start, end, median = 0, x, 0

        # We know
        # partitionx + partitiony = (x+y+1)//2

        while start <= end:
            # px -> partitionx and py -> partitiony
            px = start + (end - start) // 2
            py = (x + y + 1) // 2 - px

            # leftx, rightx -> edge elements on nums1
            # lefty, righty -> edge elements on nums2
            leftx, rightx, lefty, righty = 0, 0, 0, 0
            leftx = minV if px == 0 else nums1[px - 1]
            rightx = maxV if px == x else nums1[px]

            lefty = minV if py == 0 else nums2[py - 1]
            righty = maxV if py == y else nums2[py]

            if leftx <= righty and lefty <= rightx:
                # We found the spot for median
                if (x + y) % 2 == 0:
                    median = (max(leftx, lefty) + min(rightx, righty)) / 2
                    return median
                else:
                    median = max(leftx, lefty)
                    return median
            elif leftx > righty:
                # We are too much in the right, move towards left
                end = px - 1
            else:
                # We are too much in the left, move towards right
                start = px + 1
        return -1
