"""
	题目：将第015题中的xls格式的城市数据写入xml中
	解析：
		1. python中xls的读取
		2. xml的创建和写入
	步骤：
		1. 导入库函数
		2. 读取xls文档
		3. 创建xml文档并写入
"""
# 导入庫函数
import os
import xlrd
import xml.dom.minidom
import json
from html.parser import HTMLParser


# 读取xls文档
def read_xls(paths):
	workbook = xlrd.open_workbook(paths)  # 打开xls文件并放入到workbook中
	worksheet = workbook.sheets()[0]  # 取出workbook中的sheet
	data_dict = {}  # 设置一个字典变量用于存储sheet中返回的数据
	for row in worksheet.get_rows():
		data_list = [col.value for col in row]  # 用data_list保存sheet的每行信息
		data_dict[data_list[0]] = data_list[1:]  # 将data_list[0]作为字典的键，使用切片获取data_list[1]之后的数据
	return data_dict


# 创建xml文档并写入
def wt_xml(data, save_paths):
	# 创建标签
	annotations = '''
	<!--
	城市信息
	"序号":[城市]
	-->
	'''
	# 将标签和内容合并
	# json.dumps用于将字典形式的数据转换为字符串，常用于将数据写入到json文档中
	# json.loads用于将字符串形式的数据转换为字典，常用于读取json文档中的数据
	# json文档不可存储字典形式的数据
	content = annotations + (json.dumps(data, indent=4, ensure_ascii=False ))
	# 创建空文档
	doc = xml.dom.minidom.Document()
	# 创建根节点
	root = doc.createElement('root')
	# 将根节点加入到文档对象中
	doc.appendChild(root)
	# 创建城市节点
	city = doc.createElement('city')
	# 将城市节点加入到根节点中
	root.appendChild(city)
	# 创建文档节点
	text = doc.createTextNode(content)
	# 将文档节点写入到城市节点中
	city.appendChild(text)
	# 保存
	with open(save_paths, 'w', encoding='utf-8') as f:  # 打开保存路径的文档，并用变量f接受，如果不存在就创建
		html_paser = HTMLParser()  # 定义html解析文本变量
		result = html_paser.unescape(doc.toxml())  # 处理html文档中的转义字符
		f.write(result)  # 将处理后的结果写入到f中


if __name__ == '__main__':
	os.chdir('/home/boni/Desktop/practice_018')  # 切换到当前目录下
	path = '/home/boni/Desktop/practice_018/practice_018.xls'  # 用于读取xls文档的路径
	save_path = '/home/boni/Desktop/practice_018/practice_018.xml'  # 用于存储xml结果的路径
	dict_ = read_xls(path)
	wt_xml(dict_, save_path)
