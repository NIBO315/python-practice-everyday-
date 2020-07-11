"""
	题目： 将第014题生成的学生xls格式信息写入到xml格式的文档中
	解析：
		1. python中xls文档的读取
		2. python中xml文档的创建、写入
	步骤：
		1. 导入庫函数
		2. 定义xls文档读取函数
		3. 定义xml文档写入函数
"""
# 导入庫函数
import os
import xlrd
import xml.dom.minidom
import json
from html.parser import HTMLParser


# xls文档读取函数
def read_xls(paths):
	workbook = xlrd.open_workbook(paths)
	worksheet = workbook.sheets()[0]
	data_dict = {}
	for row in worksheet.get_rows():
		data_list = [col.value for col in row]
		data_dict[data_list[0]] = data_list[1:]
	return data_dict


# xml文档写入函数
def wt_xml(data, save_paths ):
	'''创建xml文档并写入'''
	'''----------------------------------'''
	# 创建标签
	annotation = '''
	<!--
	学生信息表
	"id": [名字, 语文, 英语, 数学]
	-->
	'''
	# 将内容和标签合并
	content = annotation + (json.dumps(data, indent=4, ensure_ascii=False))
	# 创建空文档
	doc =xml.dom.minidom.Document()
	# 创建根节点
	root = doc.createElement('root')
	# 将根节点添加到文档对象中
	doc.appendChild(root)
	# 创建学生节点
	student = doc.createElement('student')
	# 将学生节点添加到根节点上
	root.appendChild(student)
	# 创建文本节点
	text = doc.createTextNode(content)
	# 将文本节点添加到学生节点上
	student.appendChild(text)
	'''------------------------------------------'''
	# 保存
	with open(save_paths, 'w', encoding='utf-8') as f:
		html_parser = HTMLParser()
		result = html_parser.unescape(doc.toxml())
		f.write(result)


if __name__ == '__main__':
	os.chdir('/home/boni/Desktop/practice_017')
	path = '/home/boni/Desktop/practice_017/practice_017.xls'
	save_path = '/home/boni/Desktop/practice_017/practice_017.xml'
	dict_ = read_xls(path)
	wt_xml(dict_, save_path)
