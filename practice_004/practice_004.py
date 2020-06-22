"""
	题目：将任何一个纯英文文本内的单词提取，并统计其出现次数
	解析:
		正则表达式的使用
		字典默认值的使用
		对字典的遍历
		排序算法
	步骤：
		1. 导入库函数
		2. 读取英文文本
		3. 用正则表达式进行处理，将单词分割开
		4. 使用字典进行统计
		5. 根据字典值进行排序

"""
# 导入庫函数
import re
from collections import defaultdict

if __name__ == '__main__':
	# 读取英文文本
	with open("test.txt", 'r', encoding='utf-8') as fp:
		data = fp.read()
	data = data.lower()  # 将所有字母小写
	# 正则表达式处理
	f = re.split(r',|;|:|\s|-|\n|\.', data)
	# 使用字典统计
	count = 0
	for i in f:  # 统计单词数
		count+=1
	print(count)

	dict = defaultdict(int)
	for words in f:
		dict[words]+=1
	del dict['']

	# 进行排序
	dict = sorted(dict.items(), key=lambda item:item[1],reverse=True)
	for key, value in dict:
		print("%s:%d" % (key, value))
