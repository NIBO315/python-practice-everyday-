"""
    题目：将第016题的xls格式数字信息写入到xml格式的文档中
    解析：
        1. xls文件的读取操作
        2. xml文件的创建和写入
    步骤：
        1. 导入函数库
        2. 定义xls文件读取函数
        3. 定义xml文件创建写入函数
"""
# 导入庫函数
import os
import xlrd
import json
import xml.dom.minidom
from html.parser import HTMLParser


# xls文件的读取
def rd_xls(paths):
    workbook = xlrd.open_workbook(paths)
    worksheet = workbook.sheets()[0]
    data_dict = {}
    for row in worksheet.get_rows():
        data_list = [col.value for col in row]
        data_dict[data_list[0]] = data_list[1:]
    return data_dict


# xml文件的创建和写入
def wb_xml(data, save_paths):
    # 创建标签
    annotations = '''
    <!--
    数字信息表
    '序号':[数字1,数字2,数字3]
    -->
    '''
    # 内容
    content = annotations + (json.dumps(data, indent=4, ensure_ascii=False))
    # 创建空文档
    doc = xml.dom.minidom.Document()
    # 创建根节点
    root = doc.createElement('root')
    # 将根节点加入到文件对象下
    doc.appendChild(root)
    # 创建数字节点
    numbers = doc.createElement('numbers')
    # 将数字节点加入到根节点下
    root.appendChild(numbers)
    # 创建内容节点
    text = doc.createTextNode(content)
    # 将内容节点写入到数字节点下
    numbers.appendChild(text)
    # 保存
    with open(save_paths, 'w', encoding='utf-8') as f:
        html_parser = HTMLParser()
        result =html_parser.unescape(doc.toxml())
        f.write(result)


if __name__ == '__main__':
    os.chdir('/home/boni/Desktop/practice_019')
    path = '/home/boni/Desktop/practice_019/practice_019.xls'
    save_path = '/home/boni/Desktop/practice_019/practice_019.xml'
    dict_ = rd_xls(path)
    wb_xml(dict_, save_path)
