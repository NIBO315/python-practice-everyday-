"""
	题目：一个HTML文件，找出里面的链接。
	解析：
		1. python文件操作
		2. python爬虫库BeautifulSoup的使用
	步骤：
		1. 导入庫函数
		2. 定义文件读取函数
		3. 定义Html解析函数
		4. 主函数循环
"""
# 导入庫函数
import requests
from bs4 import BeautifulSoup
import re


# 定义文件读取函数
def get_html_text(url):
	try:
		# 请求链接获取html文本
		r = requests.get(url)
		# 以utf-8编码
		r.encoding = 'utf-8'
		# 返回获得的html文本
		return r.text
	except:
		return ''


# 定义Html文本解析函数
def html_parser(html, base_url):
	# 对html文本进行解析
	soup = BeautifulSoup(html, 'html.parser')
	# 设置一个set()集合
	urls = set()
	# 循环获取解析后的文本内容
	for url in soup.find_all('a'):
		try:
			# 取出url内的href属性
			url = url['href']
			# 正则表达式处理绝对路径的特殊字符
			absolute_url = r'((http|https|ftp)://)?(\w+)(\. \w+)+'
			# compile函数返回代码串
			absolute_url_pattern = re.compile(absolute_url, re.IGNORECASE)
			# match函数对compile后的代码串进行匹配
			if absolute_url_pattern.match(url):
				urls.add(url)
				continue
			relative_url = r'\.?(/\w+)+/?'
			relative_url_pattern = re.compile(relative_url)
			if relative_url_pattern.match(url):
				url = base_url + url
				urls.add(url)
				continue
		except:
			continue
	return urls


def show(urls):
	for url in urls:
		print(url)


# 主函数循环
if __name__ == '__main__':
	url = 'https://www.baidu.com/'
	html = get_html_text(url)
	urls = html_parser(html, url)
	show(urls)
