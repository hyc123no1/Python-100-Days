"""

读取CSV文件

Version: 0.1
Author: 骆昊
Date: 2018-03-13

"""

import csv

filename = 'Day01-15\\Day11\\code\\example.csv'

try:
	with open(filename) as f:
		reader = csv.reader(f)
		data = list(reader)
except FileNotFoundError:
	print('无法打开文件:', filename)
else:
	for item in data:
		print('{:<25}{:<15}{:<10}'.format(item[0], item[1], item[2]))


#format 字符串格式化
#print('{:^20}'.format('a'))#居中 :^ 宽度14
#print('{:>20}'.format('a'))# 右对齐 :> 宽度14
#print('{:<20}'.format('a')) # 左对齐 :< 宽度14
#print('{:*<20}'.format('a')) # :后边可跟填充物,只允许一个字符
#print('{:@>20}'.format('a'))
