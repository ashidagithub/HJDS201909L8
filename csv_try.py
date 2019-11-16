# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.11.16

# Description:
#   学习CSV文件的常用读写方法
# ------------------------(max to 80 columns)-----------------------------------

import csv

filename = 'test_write.csv'
repeat_times = 10

# Try to write a csv
header_data = ["行号", "列名1", "列名2"]
row_data = [1, '第1列数据', '第2列数据']  # data of a row
with open(filename, "w", encoding='utf8', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header_data)
    # writer.writerow(row_data)
    for cnt in range(repeat_times):
        row_data = [cnt, '第1列数据', '第2列数据']  # data of a row
        writer.writerow(row_data)
