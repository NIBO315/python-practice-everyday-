"""
	题目：随机生成校验码
	解析：
		1. python pillow库的使用
		2. 随机数的使用
	步骤：
		1. 导入庫函数
		2. 定义图片颜色
		3. 定义字体颜色
		4. 定义随机字体的生成
		5. 设置画布
		6. 设置画笔
		7. 在画布上画背景和字体
"""
# 导入庫函数
import os
import string
import random
from PIL import Image, ImageFont, ImageDraw, ImageFilter


# 定义背景颜色
def ran_color():
	return (random.randint(64, 255),
			random.randint(64, 255),
			random.randint(64, 255))


# 定义字体颜色
def font_color():
	return (random.randint(32, 127),
			random.randint(32, 127),
			random.randint(32, 127))


# 定义随机生成的字母数字
def rnd_font():
	s = string.ascii_letters + string.digits
	r = random.sample(s, 4)
	return r


# 切换到当前目录
os.chdir(r"/home/boni/Desktop/practice_010/")
# 定义画布
img = Image.new('RGB', (240, 60), (255, 255, 255))
# 定义验证码的字体
font = ImageFont.truetype(r"/home/boni/Downloads/pycharm-community-2019.2.3/jbr/lib/fonts/DroidSans-Bold.ttf", 40)
# 定义画笔
draw = ImageDraw.Draw(img)
# 用画笔在画布上画出背景色(每一个点为一个像素并随机附上颜色)
for x in range(240):
	for y in range(60):
		draw.point((x, y), fill=ran_color())
# 得到要画在画布上的字符
print(rnd_font)
# 将字符序列化,画在画布上,并填充颜色
for i, f in enumerate(rnd_font()):
	draw.text((60*i+10, 10), f, font=font, fill=font_color())
# 对生成的校验码图片进行模糊处理
img = img.filter(ImageFilter.BLUR)
# 显示生成的校验码
img.show()
# 保存为jpeg格式
img.save('010.jpg', 'jpeg')
