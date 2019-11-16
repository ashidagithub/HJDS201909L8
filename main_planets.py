# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.11.16

# Description:
#   编制行星数据分析 （主程序）
# ------------------------(max to 80 columns)-----------------------------------

from pkg_planets.func_planets import cal_V, cal_P, cal_g, cal_Ve

# 行星的基础数据， （D,M)
Mercury = (4878, 3.02E+23)

Mercury_V = cal_V(Mercury[0] / 2)
print(Mercury_V)
