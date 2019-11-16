# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.11.16

# Description:
#   编制行星数据分析 （主程序）
# ------------------------(max to 80 columns)-----------------------------------

from pkg_planets.func_planets import cal_V, cal_P, cal_g, cal_Ve
from log_try import mylog

# 行星的基础数据， （D,M)
Mercury = (4878, 3.02E+23)
M = Mercury[1]
r = Mercury[0] / 2

Mercury_V = cal_V(r)
#print(Mercury_V)
mylog('I', Mercury_V)


Mercury_P = cal_P(M, r)
Mercury_g = cal_g(M, r)
Mercury_Ve = cal_Ve(M, r)
