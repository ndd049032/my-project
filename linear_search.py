import unittest

class Solution:
    def linear_search(self, arr: list[int], target: int) -> int:
        """
        Performs a linear search on a list and returns the index of the target value.
        If the target is not found, it returns -1.
        
        :param arr: The list to search through
        :param target: The value to search for
        :return: The index of the target value, or -1 if not found
        """
        for i in range(len(arr)):
            if arr[i] == target:
                return i  # Return the index when the target is found
        return -1  # Return -1 if the target is not found

class TestSolution(unittest.TestCase):

    def test_linear_search_found(self):
        sol = Solution()
        arr = [5, 3, 8, 4, 6]
        target = 4
        self.assertEqual(sol.linear_search(arr, target), 3)  # The target value is found at index 3

    def test_linear_search_not_found(self):
        sol = Solution()
        arr = [5, 3, 8, 4, 6]
        target = 7
        self.assertEqual(sol.linear_search(arr, target), -1)  # The target value is not found, returns -1

    def test_linear_search_first_element(self):
        sol = Solution()
        arr = [5, 3, 8, 4, 6]
        target = 5
        self.assertEqual(sol.linear_search(arr, target), 0)  # The target value is the first element, index 0

    def test_linear_search_last_element(self):
        sol = Solution()
        arr = [5, 3, 8, 4, 6]
        target = 6
        self.assertEqual(sol.linear_search(arr, target), 4)  # The target value is the last element, index 4

    def test_linear_search_empty_list(self):
        sol = Solution()
        arr = []
        target = 5
        self.assertEqual(sol.linear_search(arr, target), -1)  # An empty list returns -1

if __name__ == '__main__':
    unittest.main()
