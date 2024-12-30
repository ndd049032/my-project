import unittest

class Solution:
    def linear_search(self, arr: list[int], target: int) -> int:
       """
        執行線性搜索，並返回目標值的索引。
        如果未找到目標值，則返回 -1。
        
        :param arr: 要進行搜尋的列表
        :param target: 要搜尋的目標值
        :return: 目標值的索引，如果未找到則返回 -1
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
