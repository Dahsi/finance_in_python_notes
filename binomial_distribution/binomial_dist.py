# -*- coding:utf-8 _*-
""" 
@author:alanchc  
@file: binomial_dist.py 
@create time: 2020/11/22
@Reference:
- <<Python 股票量話交易從入門到實踐>>
- numpy.random.binomial:
https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.binomial.html#numpy.random.Generator.binomial
"""

import matplotlib.pyplot as plt
plt.style.use('ggplot')

import numpy as np



def simpmarket(
        win_rate, initial_capital=1000, play_cnt=1000, stock_num=9, position=0.01, commision=0.0002, lever=False
):
    """
    背景：
    假設一個簡易的市場，具有漲跌隨機波動特徵的短線交易市場，會不停交易，而且不需手續費
    Argument:
        initial_capital 初始投入資金
        win_rate 概率
        play_cnt 賭局次數
        stock_num 股票數量
        position 倉位比例
        commision 手續費
        lever 加註標誌

    np.random.binomial
        parameters:
            n : int or array_like of ints. Parameter of the distribution, >= 0. Floats are also accepted,
                but they will be truncated to integers.
            p : float or array_like of floats.Parameter of the distribution, >= 0 and <=1.
            size : int or tuple of ints, optional
        returns:
            out : ndarray or scalar.Drawn samples from the parameterized binomial distribution,
                  where each sample is equal to the number of successes over the n trials.
    """
    my_money = np.zeros(play_cnt)
    my_money[0] = initial_capital
    lose_cnt = 1
    binomial = np.random.binomial(stock_num, win_rate, play_cnt)

    for i in range(1, play_cnt):
        if my_money[i-1] * position * lose_cnt <= my_money[i-1]:
            once_chip = my_money[i-1] * position * lose_cnt
        else:
            print(my_money[i-1])
            break
        if binomial[i] > stock_num//2:
            my_money[i] = my_money[i-1] + once_chip if lever == False else my_money[i-1] + once_chip * lose_cnt
            lose_cnt = 1
        else:
            my_money[i] = my_money[i-1] - once_chip if lever == False else my_money[i - 1] - once_chip * lose_cnt
            lose_cnt += 1
        my_money[i] -= commision
        if my_money[i] <= 0:
            break

    return my_money

def binomial_case():
    """
    假設盈利機率為 50%，請 50 人参與 1000 局交易
    :return:
    """
    trader = 50
    play_cnt = 1000
    commision = 0.01
    initial_capital = 10000
    trader_dict = {i: simpmarket(0.5, initial_capital=initial_capital, play_cnt=play_cnt, stock_num=9, commision=commision)
                   for i in np.arange(0, trader)}
    _ = [plt.plot(np.arange(play_cnt), trader_dict[i]) for i in trader_dict]  # 繪製取線圖
    _ = plt.hist([trader_dict[i][-1] for i in trader_dict], bins=30)  # 繪製直方圖

    return True

def positmanage(win_rate, initial_capital, play_cnt, stock_num, commission):
    my_money = np.zeros(play_cnt)
    my_money[0] = initial_capital
    binomial = np.random.binomial(stock_num, win_rate, play_cnt)
    for i in range(1, play_cnt):
        once_chip = my_money[i-1] * (win_rate * 1 - (1-win_rate))/1  # 凱利公式下註
        if binomial[i] > stock_num//2:
            my_money[i] = my_money[i-1] + once_chip
        else:
            my_money[i] = my_money[i - 1] - once_chip
        my_money[i] -= commission * once_chip
        if my_money[i] < 0:
            break
    return my_money


def binomial_with_kelly_formula():
    trader = 50
    play_cnt = 30
    initial_capital = 1000
    win_rate = np.random.uniform(0.25, 1)
    commision = 0.0002
    stock_num = 9
    trader_dict = {
        i: positmanage(win_rate, initial_capital, play_cnt, stock_num, commision)
        for i in np.arange(0, trader)}
    _ = [plt.plot(np.arange(play_cnt), trader_dict[i]) for i in trader_dict]  # 繪製取線圖
    _ = plt.hist([trader_dict[i][-1] for i in trader_dict], bins=30)  # 繪製直方圖

    return True


# --------------------------------------------------------------------------------
if __name__ == '__main__':
    binomial_case()
    binomial_with_kelly_formula()
