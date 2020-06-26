"""
	题目：统计一个文件夹下所有的日记文档，提取出每篇文章出现频率较高的词
	解析：
		1. python os对文件的操作
		2. re正则化的使用
		3. 字典的使用
	步骤：
		1. 导入庫函数
		2. 设置读取文件列表和存储文件列表
		3. 定义文件处理函数
		4. 定义每个文件单词统计函数
"""
# 导入库
import os
import re
from collections import defaultdict

# 切换路径
path = "/home/boni/Desktop/practice_006/txt/"
os.chdir(path)
# 定义文件读取和存储列表
list_ = []
fist_ = []
# 设置忽略词
ignore_words = ['i', 'I', 'my', 'the', 'by', 'and', 'should'
				, 'am', 'for', 'in', 'to', 'of', 'so', 'we', 'was'
				, 'do', 'me', 'have', 'it']
# 获取文件目录
list_ = os.listdir(path)


# 定义文件处理函数
def process_file():
	# 遍历列表寻找后缀名为.txt的文档，并加入到fist_列表中
	for i in list_:
		if os.path.splitext(i)[1] == '.txt':
			fist_.append(i)


# 定义每个文件单词统计函数
def count(filename):
	# 打开每个txt文档
	with open(filename, 'r') as fp:
		# 去除特殊字符
		data = fp.read()
		# 变为小写字母
		data = data.lower()
		data = re.split(r':|/|;|\.|!|\s|-|,', data)
		# print(type(data))
	# 构建字典
	dict = defaultdict(int)
	# 遍历data列表中的字符串，如果是忽略词就跳过
	# 否则就加入字典的键同时值+1
	for words in data:
		if words in ignore_words:
			continue
		else:
			dict[words] += 1
	del dict['']
	# print(type(dict))
	dict = sorted(dict.items(), key=lambda item: item[1], reverse=True)
	# print(type(dict))
	print(dict[0])


if __name__ == '__main__':
	process_file()
	for i in fist_:
		count(i)
