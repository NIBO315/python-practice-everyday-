"""
	题目： 一个Html文件，找出里面的正文
	解析：
		爬虫的基本使用：
			requests获取URL网页界面
			Beautiful soup对获取的内容进行解析
	步骤：
		1. 导入函数库
		2. 请求获取文本
		3. 对文本进行解析
"""

# 导入庫函数
import requests
from bs4 import BeautifulSoup


def get_text():
	# 需要获取的URL网页地址
	url = 'http://news.qq.com/'
	# 请求获取文本
	wbtext = requests.get(url).text
	# 对获取的文本进行解析
	soup = BeautifulSoup(wbtext, 'lxml')
	# 清除script
	[script.extract() for script in soup.find_all('script')]
	[style.extract() for style in soup.find_all('style')]
	print(soup.title)
	print(soup.find_all('body'))
	# return soup.get_text()


if __name__ == '__main__':
	print(get_text())

