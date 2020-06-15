import base64

numbers = {
	'id': '1234',
	'goods': '1000'
}


# 生成激活码
def gen_ACode(id, goods):
	numbers['id'] = id
	numbers['goods'] = goods
	rw = '/'.join([k+':'+v for k, v in numbers.items()])
	rw_b64 = base64.urlsafe_b64encode(rw.encode('utf-8'))
	c_code = rw_b64.decode()
	return c_code


# 保存激活码
def save_ACode(c_code):
	with open('keycode.txt', 'a+') as fp:
		fp.write(c_code + '\n')


# 显示激活码
def show(c_code):
	print(c_code + '\n')


# 解析激活码
def find_goods():
	a = input("input code:")

	with open('keycode.txt', 'r', encoding='utf-8') as f:
		lines = f.readlines()
		for i in range(200):
			# strip('char') 去除首尾指定字符
			# 用于消除字符串后的换行符'\n'
			if lines[i].strip() == a.strip():
				c = base64.urlsafe_b64decode(lines[i].encode('utf-8'))
				print(c)
				return
		print("valid code")


def get_all():
	for i in range(1000, 1200):
		c_code = gen_ACode(str(i), str(i/2))
		save_ACode(c_code)
		show(c_code)


if __name__ == '__main__':
	get_all()
	find_goods()
