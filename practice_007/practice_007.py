"""
	题目： 有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。
	解析： 
		1. os对文件的操作
		2. 正则表达式的使用
	步骤：
		1. 导入库函数
		2. 定义读取文件目录函数
		3. 定义读取文档内容函数 
"""
# 导入庫函数
import os


# 定义读取目录函数
def getfile(paths):
	file = os.listdir(paths)
	file_list = []
	for i in file:
		if os.path.splitext(i)[1] == '.py':
			file_list.append(i)
	return file_list


# 定义读取文档内容函数
def count_line(filename):
	# 统计总行数、空白行、注释行
	total_lines, blank_lines, comment_lines = 0, 0, 0
	m = 1  # 用于记录“”“出现的个数，如果是奇数则表示为多行注释的开始，如果是偶数则表示多行注释的结束
	with open(filename, 'r') as fp:
		lines = fp.readlines()
		for line in lines:
			total_lines += 1
			fline = line.strip()
			if not fline:
				blank_lines += 1
			elif fline.startswith('#'):
				comment_lines += 1
			elif fline.startswith('"""') or fline.startswith("'''"):
				comment_lines += 1
				if m % 2 == 0:
					continue
				m += 1
				j = lines.index(line)
				for k in range(j+1, len(lines)):
					if "'''\n" in lines[k] or '"""\n' in lines[k]:
						break
					comment_lines += 1

	code_lines = total_lines - comment_lines - blank_lines
	# print(total_lines)
	# print(comment_lines)
	# print(blank_lines)
	print("name:", filename)
	print("code_lines:", code_lines)
	print("comment_lines:", comment_lines)
	print("blank_lines:", blank_lines)
	return code_lines, comment_lines, blank_lines


if __name__ == '__main__':
	path = r"/home/boni/Desktop/practice_007/007_py/"
	os.chdir(path)
	code, blank, comment = 0, 0, 0
	file_ = getfile(path)
	for i in file_:
		f = count_line(i)
		code += f[0]
		comment += f[1]
		blank += f[2]
	print("code_lines:", code)
	print("comment_lines:", comment)
	print("blank_lines:", blank)


