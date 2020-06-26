"""
	题目：存放图片的文件夹，将其图片的大小都改为iphone5分辨率的大小
	解析：
		OS的文件的读取
		python的PIL库对图片的处理
	步骤：
		1. 导入庫函数
		2. 处理图片转换函数
		3. 读取图片函数
"""
# 导入庫函数
import os
from PIL import Image
# 定义图片路径
myPath = "/home/boni/Desktop/practice_005/Picture/"
outPath = "/home/boni/Desktop/practice_005/Picture/outpicture/"


# 图片处理函数
def processImg(file_source, des_source, name, img_type):
	"""
		file_source 待转换图片存放的文件夹名称
		des_source 转换后图片输出存放的文件夹名称
		name 文件名
		img_type 文件后缀
	"""
	# 修改图片后缀名
	img_type = 'jpeg' if img_type == '.jpg' else 'png'
	# 打开图片
	im = Image.open(file_source+name)
	# 设置缩放比例
	rate = max(im.size[0]/640.0 if im.size[0] > 640 else 0, im.size[1]/1136.0 if im.size[1] > 1136 else 0)
	# 缩放图片
	if rate:
		im.thumbnail((im.size[0]/rate, im.size[1]/rate))  # 有两个括号，使得浮点数转化为元组
		print('success')
		im.save(des_source+name, img_type)
	# 存储缩放后的图片


# 读取图片函数
def read_run():
	# 切换工作目录
	os.chdir(myPath)
	# 遍历文件并返回文件名称
	for i in os.listdir(os.getcwd()):
		# 分离文件名和后缀
		postfix = os.path.splitext(i)[1]
		if postfix == '.jpg' or postfix == '.png':
			processImg(myPath, outPath, i, postfix)


if __name__ == '__main__':
	read_run()
