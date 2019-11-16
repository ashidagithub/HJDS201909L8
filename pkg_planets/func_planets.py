# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.11.16

# Description:
#   行星数据计算函数 （函数模块）
# ------------------------(max to 80 columns)-----------------------------------

import math

G = 6.67259E-11


def cal_V(r):
    '输入行星的半径，返回行星的体积'

    # 体积计算公式 V = 4/3 * pi * r3
    V = 4 / 3 * math.pi * r * r * r
    V = 4 / 3 * math.pi * math.pow(r, 3)
    V = 4 / 3 * math.pi * (r**3)

    return V


def cal_P(M, r):
    '根据质量和半径计算行星的密度'
    V = cal_V(r)
    return M / V / 1000000000000


def cal_g(M, r):
    g = M * G / r / r / 1000000
    g = M * G / (r**2) / math.pow(10, 6)
    g = M * G / math.pow(r, 2) / math.pow(10, 6)
    return g


def cal_Ve(M, r):
    Ve = math.sqrt(2 * G * M / r / 1000) / 1000
    return Ve


if __name__ == '__main__':
    V = cal_V(6371)
    print(V)

    density = cal_P(4.869E+24, 9.28E+11)
    print(density)

    g = cal_g(5.97E+24, 6371)
    print(g)

    Ve = cal_Ve(5.97E+24, 6371)
    print(Ve)
