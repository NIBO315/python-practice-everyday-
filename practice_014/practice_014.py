"""
	题目：将字典信息写入excel表格中
	解析：
		1. python文件读取操作
		2. excel表格的写入操作
	步骤：
		1. 导入庫函数
		2. 读取txt文件，并保存到字典中
		3. 建立excel表格
		4. 循环字典的键值对将其写入到对应的excel单元格位置
"""
# 导入庫函数
import os
import xlwt
import ast


# 读取txt文件，并保存到字典中
def read_txt(paths):
	with open(paths, 'r') as fp:
		list_ = fp.read()
		print(list_)
		dicts = ast.literal_eval(list_)
		return dicts


# 建立excel表格
def excel_build():
	workbooks = xlwt.Workbook(encoding='utf-8')
	sheets = workbooks.add_sheet('practice_014', cell_overwrite_ok=True)
	return workbooks, sheets


# 循环字典的键值对写入到对应的excel单元格位置
def write2excel(dict_, workbook_, sheet_, save_paths):
	key_list = []  # 保存键的列表
	value_list = []  # 保存值的列表
	for key, value in dict_.items():
		key_list.append(key)
		value_list.append(value)

	row_key = 0
	for key in key_list:
		sheet_.write(row_key, 0 ,key)
		row_key += 1

	row_value = 0
	for value in value_list:
		col_value = 1
		for i in value:
			sheet_.write(row_value, col_value, i)
			col_value += 1
		row_value += 1
	workbook_.save(save_paths)


if __name__ == '__main__':
	os.chdir('/home/boni/Desktop/practice_014/')
	path = 'practice_014.txt'
	save_path = '/home/boni/Desktop/practice_014/practice_014.xls'
	dict = read_txt(path)
	workbook, sheet = excel_build()
	write2excel(dict, workbook, sheet, save_path)
