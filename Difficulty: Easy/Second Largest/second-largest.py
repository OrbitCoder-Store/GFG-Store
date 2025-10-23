class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        arr = list(set(arr))
        arr.sort()
        return -1 if len(arr)<2 else arr[-2]