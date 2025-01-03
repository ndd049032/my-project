import unittest
class Solution:
    def search_closest(self, nums: list[int], target: int) -> int:
         """
        搜尋一個有序數列中最接近目標值的數字。
        如果目標值存在，則直接返回該數字；如果目標值不在數列中，則返回小於目標值且最接近的數字。
        
        :param nums: 要搜尋的有序數列
        :param target: 目標值
        :return: 返回目標值或最接近目標值的數字
        """
        if not nums:
            return None
        if target < nums[0]:
            return None
        if target > nums[-1]:
            return nums[-1]


        i, j = 0, len(nums) - 1
        closest = None

        while i <= j:
            m = i + (j - i) // 2 
            if nums[m] < target:
                closest = nums[m]
                i = m + 1
            elif nums[m] > target:
                j = m - 1
            else:
                return nums[m]

        return closest


class TestSolution(unittest.TestCase):

    def test(self):
        sol = Solution()

       
        nums = [1, 3, 5, 6, 8, 10]
        target = 6
        self.assertEqual(sol.search_closest(nums, target), 6)  # 目標值在數組中

        
        nums = [1, 3, 5, 6, 8, 10]
        target = 7
        self.assertEqual(sol.search_closest(nums, target), 6)  # 7 不在數組中，返回最接近的 6

       
        nums = [1, 3, 5, 6, 8, 10]
        target = 12
        self.assertEqual(sol.search_closest(nums, target), 10)  # 目標值大於所有數字，返回最大值

       
        nums = [1, 3, 5, 6, 8, 10]
        target = 0
        self.assertEqual(sol.search_closest(nums, target), None)  # 目標值小於所有數字，返回 None

       
        nums = []
        target = 5
        self.assertEqual(sol.search_closest(nums, target), None)  # 空列表，返回 None


if __name__ == '__main__':
    unittest.main()
