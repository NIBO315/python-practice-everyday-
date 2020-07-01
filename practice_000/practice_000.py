"""
题目描述：在图片的右上角添加一个数字
题目解析：
	涉及知识：图像处理
			文件读取和存储
步骤：
	1.导入所需的库（PIL）
	2.定义生成数字的函数
		2.1 将图片设为画布
		2.2 设置数字的大小和颜色
		2.3 获取图片的宽和高
		2.4 将数字画在图片的右上角
		2.5 保存画好的图片并返回给主函数
	3.执行主函数
		3.1 导入图片
		3.2 调用函数
		3.3 显示函数
函数解析：
	ImageDraw.Draw(image) - 创建一个可以在给定图像上绘画的对象，俗称画笔（有返回值）
	draw.arc(xy,start,end,options) - 在指定的区域，从start到end绘制一条弧;xy是一个四元组，表示左上角和右下角的坐标;start和end表示绘制弧的大小（-360，360）;options设置弧的颜色（无返回值）
	draw.text(position,string,options) - position表示绘制的位置，默认从左上角;string表示绘制的内容;options表示绘制的颜色，常用fill填充（无返回值）
	ImageFont.truetype(file,size) - 加载一个TrueType或者OpenType的字体文件（file）,并创建一个指定大小（size）的字体对象（有返回值）
	ImageColor.colormap.get(options) - 从颜色映射图中获取颜色
	Image.show() - 在图片查看工具上显示当前操作的image对象
	Image.open(filename) - 打开图片文件或其所在位置
"""

# 从PIL库导入Image等
from PIL import Image, ImageFont, ImageColor, ImageDraw


# 定义生成图像的函数
def add_text(image, text):
	# 将图片定义为画布
	draw = ImageDraw.Draw(image)
	# 定义数字的大小和颜色
	font = ImageFont.truetype('/home/boni/Downloads/pycharm-community-2019.2.3/jbr/lib/fonts/DroidSans-Bold.ttf', 35)   # (字体，字号，编码方式)
	color = ImageColor.colormap.get("red")
	# 获取图片的宽和高
	width, height = image.size
	# 将数字画在图片右上角
	draw.arc((width-40, 20, width, 60), 0, 360, 'pink', 70)
	draw.text((width-30, 20), text, color, font)
	# 显示图片
	image.show()
	# 保存图片
	# image.save('/home/boni/Pictures/xiaoxin.png')


if __name__ == '__main__':
	# 导入图片
	image = Image.open('/home/boni/Pictures/xiaoxin.png')
	# 设置添加的数字
	text = '6'
	# 调用函数
	add_text(image, text)


