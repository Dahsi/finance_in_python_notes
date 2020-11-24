# -*- coding:utf-8 _*-
""" 
@author:alanchc  
@file: binomial_dist.py 
@create time: 2020/11/22
@Reference:
完整 medium 文章:
https://medium.com/finance-in-python-notes/binomial-distribution-%E5%9C%A8%E9%87%8F%E5%8C%96%E4%BA%A4%E6%98%93%E7%9A%84%E4%BD%9C%E7%94%A8-fd9c0fdd0bc6
- <<Python 股票量化交易從入門到實踐>>
- numpy.random.binomial:
https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.binomial.html#numpy.random.Generator.binomial
"""

import matplotlib.pyplot as plt
plt.style.use('ggplot')

import numpy as np

def position_manage(win_rate, odds, initial_capital, play_cnt, stock_num, commission):
    """
    Argument:
        trader 重複次數
        play_cnt 股票組合持有天數
        initial_capital 初期投入資金
        win_rate 上漲勝率
        commision 手續費
        stock_num 股票種類
        odds 賠率
    returns:
        list: my_money 每日總資金
    """
    my_money = np.zeros(play_cnt)
    my_money[0] = initial_capital
    binomial = np.random.binomial(stock_num, win_rate, play_cnt)
    for i in range(1, play_cnt):
        once_chip = my_money[i-1] * (win_rate * odds - (1-win_rate))/odds  # 凱利公式下註
        if binomial[i] > stock_num//2:
            my_money[i] = my_money[i-1] + once_chip
        else:
            my_money[i] = my_money[i - 1] - once_chip
        my_money[i] -= commission * once_chip
        if my_money[i] < 0:
            break
    return my_money


def binomial_with_kelly_formula():

    trader = 10  # 重複次數
    play_cnt = 30  # 股票組合持有天數
    initial_capital = 10000  # 初期投入資金
    win_rate = 0.55 # np.random.uniform(0.25, 1)  # 上漲勝率
    commision = 0.0002  # 手續費
    stock_num = 5  # 股票種類
    odds = 1  # 賠率

    trader_dict = {
        i: position_manage(win_rate, odds, initial_capital, play_cnt, stock_num, commision)
        for i in np.arange(0, trader)}
    _ = [plt.plot(np.arange(play_cnt), trader_dict[i]) for i in trader_dict]  # 繪製取線圖
    _ = plt.hist([trader_dict[i][-1] for i in trader_dict], bins=2)  # 繪製直方圖

    return True


# --------------------------------------------------------------------------------
if __name__ == '__main__':
    binomial_with_kelly_formula()
