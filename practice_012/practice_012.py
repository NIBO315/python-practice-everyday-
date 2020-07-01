"""
    题目：当输入敏感词汇时，将用*号代替
    解析：
        1. 文件的读取
        2. replace函数的使用
    步骤：
        1. 导入庫函数
        2. 定义敏感词汇文本读取函数
        3. 定义输入替换敏感词汇函数
"""
# 导入庫函数
import os


# 定义敏感词汇文本文件读取函数
def get_filter(paths):
    with open(paths) as fp:
        lines = fp.readlines()
    word = []
    for w in lines:
        word.append(w.strip('\n'))
    return word


# 替换输入的敏感词汇
def replace_filters(wds):
    scan = input("please input words:")
    for i in wds:
        scan = scan.replace(i, '*'*len(i))
    return scan


if __name__ == '__main__':
    # 切换到当前目录
    os.chdir(r'/home/boni/Desktop/practice_012/')
    # 设置读取文档的路径
    path = '/home/boni/Desktop/practice_012/filtered_words.txt'
    # 得到敏感词汇列表
    words = get_filter(path)
    # 得到替换后的敏感词汇列表
    replace_words = replace_filters(words)
    # 打印
    print(replace_words)
