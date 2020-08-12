# Python program to sum a list
# Time Complexity : O(n)
# Space Complexity : O(1)
from typing import List


class Solution:

    def runningSum(self, nums: List[int]) -> List[int]:
        solution = []
        j = 0
        for i in nums:
            j += i
            solution.append(j)
        return solution


# Driver program to test above functions
if __name__ == '__main__':

    test = Solution()
    list2 = [1, 2, 3, 4, 5]
    listResult = test.runningSum(list2)

    print("\nRunning total")
    print(str(listResult)[1:-1])