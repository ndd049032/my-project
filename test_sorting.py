import random
import matplotlib.pyplot as plt
import unittest

def bubble_sort(arr, update_func):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j] 
                update_func(arr)

# 可視化商品價格排序
def visualize_sorting():
    arr = [random.randint(1, 100) for _ in range(20)]  # 隨機生成商品價格
    fig, ax = plt.subplots()
    bar_rects = ax.bar(range(len(arr)), arr, align="center")
    ax.set_ylabel('Price')
    ax.set_xlabel('Item Index')

    def update_fig(arr):
        for rect, val in zip(bar_rects, arr):
            rect.set_height(val)
        plt.pause(0.1)

    bubble_sort(arr, update_fig)  # 啟動排序
    plt.show()  # 顯示排序過程

# 測試
class TestSorting(unittest.TestCase):

    def test_bubble_sort(self):
        arr = [64, 34, 25, 12, 22, 11, 90]
        expected = sorted(arr)
        bubble_sort(arr, lambda x: None)  # 測試排序邏輯
        self.assertEqual(arr, expected)  # 驗證排序結果是否正確

    def test_empty_list(self):
        arr = []
        bubble_sort(arr, lambda x: None)
        self.assertEqual(arr, [])  # 空列表應該還是空

    def test_single_element_list(self):
        arr = [5]
        bubble_sort(arr, lambda x: None)
        self.assertEqual(arr, [5])  # 單個元素列表不應該改變

if __name__ == '__main__':
    unittest.main()

