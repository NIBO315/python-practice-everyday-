"""
环境配置：Linux下安装Redis和Redis-server
题目：将0001题生成的激活码存储到Redis中
解析：Redis的使用
步骤：
	1.导入库
	2.连接redis池
	3.打开文件并读取每行内容
	4.对每行内容进行解码
	5.进行正则化
	6.读入redis中
"""
# 导入库函数
import redis
import base64

if __name__ == '__main__':
	# 连接redis池
	pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
	r = redis.Redis('localhost', port=6379, db=0)
	print('connect success')
	# 读取文件
	with open('keycode.txt', 'r') as fp:
		for line in fp.readlines():  # 读取每一行
			# 对内容进行解码
			s = base64.urlsafe_b64decode(line.encode('utf-8'))
			# 去除字符串末尾的空字符并解码以去除开头的b
			s = s.strip().decode()
			# print(type(s))
			# print(s)
			# print(len(s))
			# 截取字符串的对应长度作为对应的键值对
			r.set(s[0:7], s[8:])
		# print(r.get('id:1199').decode())
	print("insert success")
