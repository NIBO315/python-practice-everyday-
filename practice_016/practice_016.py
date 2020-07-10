"""
	题目： 将txt内容写入excel表格中
	解析：
		1. python文件操作
		2. xlwt库的使用
	步骤：
		1. 导入函数库
		2. 定义文件读取函数
		3. 定义建立表格函数
		4. 定义文件写入函数
"""
# 导入庫函数
import os
import xlwt
import json


# 定义文件读取函数
def read_txt(paths):
	with open(paths, 'r') as fp:
		list_ = json.load(fp)
		# print(list_)
		# print(len(list_))
	return list_


# 定义建立表格函数
def build_sheet():
	workbook = xlwt.Workbook(encoding='utf-8')
	sheet = workbook.add_sheet('practice_016', cell_overwrite_ok=True)
	return workbook, sheet


# 定义文件写入函数
def wb_excel(heads, lists, workbooks, sheets, save_paths):
	# 将标题写入
	for head in range(0, len(heads)):
		sheets.write(0, head, heads[head])
	# 写入序号
	row = 1
	for k in range(1, len(lists)+1):
		sheets.write(row, 0, k)
		row += 1
	# 将数据写入sheet中
	row_value = 1
	for value in lists:
		col = 1
		for i in value:
			sheets.write(row_value, col, i)
			col += 1
		row_value += 1
	# 保存
	workbooks.save(save_paths)


if __name__ == '__main__':
	os.chdir('/home/boni/Desktop/practice_016')
	path = '/home/boni/Desktop/practice_016/practice_016.txt'
	save_path = '/home/boni/Desktop/practice_016/practice_016.xls'
	list_ = read_txt(path)
	workbook, sheet = build_sheet()
	head = ['序号', '数字1', '数字2', '数字3']
	wb_excel(head,list_, workbook, sheet, save_path)