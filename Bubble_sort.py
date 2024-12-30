import random
import matplotlib.pyplot as plt

# 冒泡排序
def bubble_sort(arr, update_func):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j] 
                update_func(arr) 

# 可視化
def visualize_sorting():
    arr = [random.randint(1, 100) for _ in range(20)]
    fig, ax = plt.subplots()
    bar_rects = ax.bar(range(len(arr)), arr, align="center")

    def update_fig(arr):
        for rect, val in zip(bar_rects, arr):
            rect.set_height(val)
        plt.pause(0.1)

    bubble_sort(arr, update_fig)  
    plt.show() 

visualize_sorting()
