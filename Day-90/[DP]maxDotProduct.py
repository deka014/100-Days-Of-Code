class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:

        n1 = len(nums1)
        n2 = len(nums2)
        dp = {}

        def rec(ind1,ind2):

            if ind1 >= n1 or ind2 >= n2 :
                return -10**9

            if (ind1,ind2) in dp :
                return dp[(ind1,ind2)]

            val = nums1[ind1] * nums2[ind2]

            f1 = val + rec(ind1+1,ind2+1)

            f2 = rec(ind1+1,ind2)

            f3 = rec(ind1,ind2+1)

            dp[(ind1,ind2)] = max(val,f1,f2,f3)

            return dp[(ind1,ind2)]

        return rec(0,0)
        