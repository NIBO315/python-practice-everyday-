"""
题目：生成200随机激活码
题目解析：
三种方法：random、uuid、base64
"""

# 方法1
# import random
# import string
#
# i = 0
# for i in range(200):
#     print(''.join(random.sample(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'l', 'm'
#                                     , 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#                                 , random.randint(10, 20))))
#     i = i+1

# 方法2 uuid(唯一标识码)
# 导入uuid库
import uuid

# 循环生成200个不同的激活码
# for i in range(200):
#     # uuid.uuid1([node[,clock_seq]])
#     # node参数未指定，系统将自动调取getnode()函数获取主机硬件地址
#     # clock_seq参数未指定，系统将会随机产生14位序列号来代替
#     seq = str(uuid.uuid1())
#     # .split('-'),以‘-’为分割符，分割字符串
#     # .join()，将字符连接起来
#     string = ''.join(seq.split('-'))
#     # with as 自动关闭文件
#     # open('file','model'), a表示追加，文件存在则在文件末尾追加，文件不存在则创建文件再追加
#     with open('ACode.txt', 'a') as fp:
#         fp.write(string+'\n')

# base64
import base64

# base64编码方便使用

# 通过id检验优惠券是否存在，通过goods查找商品
coupon = {
    'id': '1231',
    'goods': '0001',
}


def gen_coupon(id, goods):
    coupon['id'] = id
    coupon['goods'] = goods
    raw = '/'.join([k + ':' + v for k, v in coupon.items()])
    raw_64 = base64.urlsafe_b64encode(raw.encode('utf-8'))
    c_code = raw_64.decode()
    return c_code


def save_coupon(c_code):
    with open('coupon.txt', 'a+') as file:
        file.write(c_code + '\n')


def show_coupon(c_code):
    print('优惠码:', c_code)


def parse_coupon(c_code):
    print('解析优惠码:', base64.urlsafe_b64decode(c_code.encode('utf-8')))


def gen_all():
    for i in range(1000, 1200):
        c_code = gen_coupon(str(i), str(int(i / 2)))
        save_coupon(c_code)


if __name__ == '__main__':
    gen_all()