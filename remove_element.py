import unittest
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        給定一個數字列表 nums 和一個數值 val，該函數將移除所有等於 val 的元素，並返回去除後的數組長度。
        
        :param nums: 待處理的數字列表
        :param val: 要移除的數值
        :return: 去除 val 後數組的新長度
        """
        fast = 0
        slow = 0 
        size = len(nums)
      
        while fast < size: 
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1 
            fast += 1

        return slow


class TestSolution(unittest.TestCase):

    def test_remove_element(self):
        sol = Solution()
        
        # 測試1: 數組 [3, 2, 2, 3] 中移除 3，預期結果是 [2, 2]，長度為 2
        nums = [3, 2, 2, 3]
        val = 3
        expected_length = 2
        new_length = sol.removeElement(nums, val)
        self.assertEqual(new_length, expected_length)
        self.assertEqual(nums[:new_length], [2, 2])  # 檢查去除後的數組內容
        
        # 測試2: 數組 [0, 1, 2, 2, 3] 中移除 2，預期結果是 [0, 1, 3]，長度為 3
        nums = [0, 1, 2, 2, 3]
        val = 2
        expected_length = 3
        new_length = sol.removeElement(nums, val)
        self.assertEqual(new_length, expected_length)
        self.assertEqual(nums[:new_length], [0, 1, 3])  # 檢查去除後的數組內容

        # 測試3: 數組 [1, 1, 1, 1] 中移除 1，預期結果是空數組，長度為 0
        nums = [1, 1, 1, 1]
        val = 1
        expected_length = 0
        new_length = sol.removeElement(nums, val)
        self.assertEqual(new_length, expected_length)
        self.assertEqual(nums[:new_length], [])  # 檢查去除後的數組內容

        # 測試4: 空數組，移除任何元素後仍應返回長度 0
        nums = []
        val = 1
        expected_length = 0
        new_length = sol.removeElement(nums, val)
        self.assertEqual(new_length, expected_length)
        self.assertEqual(nums[:new_length], [])  # 空數組應保持不變


if __name__ == '__main__':
    unittest.main()
