# -*- coding:utf-8 _*-
""" 
@author:alanchc  
@file: normal_dist.py.py 
@create time: 2020/11/26
"""

import matplotlib.pyplot as plt
plt.style.use('ggplot')

import numpy as np
# import pandas as pd

def show_normal_dist_histogram():
    """
    展示三組 normal distribution 圖。

    常用參數介紹：
    np.random.normal：
        loc 期望值
        scale 標準差
        size 基於normal distribution生成的數量

    plt.hist：
        bins: 直方圖的柱數，可選項，默認為10；
        density: 是否將得到的直方圖各 bin 的數量規一化。默認為 False；
        color：顏色序列，默認為None；
        facecolor: 直方圖顏色；
        edgecolor: 直方圖邊框顏色；
        alpha: 透明度；
        histtype: 直方圖類型，『bar』, 『barstacked』, 『step』, 『stepfilled』

    :return: None
    """
    plt.hist(np.random.normal(loc=-2, scale=0.5, size=10000), bins=50, density=True, color='g', alpha=0.5)
    plt.hist(np.random.normal(loc=0, scale=1, size=10000), bins=50, density=True, color='b', alpha=0.5)
    plt.hist(np.random.normal(loc=2, scale=1.5, size=10000), bins=50, density=True, color='r', alpha=0.5)
    plt.show()


# --------------------------------------------------------------------------------
if __name__ == '__main__':
    show_normal_dist_histogram()
    pass
