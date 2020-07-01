"""
    题目：敏感词汇文本filtered_words.txt,
        当用户输入敏感词汇时,则打印出Freedom,否则打印出HumanRights
    解析：
        1. 文件的读取
        2. 键盘的输入
    步骤：
        1. 导入庫函数
        2. 定义敏感词汇文本读取函数
        3. 判断输入词汇是否在敏感词汇文本中并给出结果
"""
# 导入庫函数
import os


# 获取敏感词文本列表
def get_filter(paths):
    with open(path, 'r') as fp:
        lines = fp.readlines()
    words_ = []
    for i in lines:
        words_.append(i.strip('\n'))
    return words_


# 判断输入是否在敏感词列表中，并给出结果
def is_filter(wds):
    scan = input('input word:')
    filter_words = wds
    flags = 0
    for i in filter_words:
        if i in scan:
            flags = 1
            break
        else:
            flags = 0
    return flags


if __name__ == '__main__':
    os.chdir(r'/home/boni/Desktop/')
    path = '/home/boni/Desktop/practice_011/filtered_words.txt'
    words = get_filter(path)
    flag = is_filter(words)
    if flag == 1:
        print('Freedom')
    if flag == 0:
        print('HumanRights')
