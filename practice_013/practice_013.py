"""
    题目：爬该网页内的图片http://tieba.baidu.com/p/2166231880
    解析：python爬虫
    步骤：
        1. 导入函数库
        2. 先得到所有的图片链接
        3. 下载链接中的图片
"""
# 导入函数库
import re
import requests
import os
import urllib.request
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw


# 获取下载文本
def get_html_text(urls):
    try:  # 防止网页不存在
        # 获取网页
        r = requests.get(urls)
        r.encoding = 'utf-8'  # 进行编码
        return r.text  # 返回网页内容
    except:
        return ''


# 处理文本文件，获取图片连接，整理为一个列表
def get_link_img(imgs_):
    # 对html文本进行解析
    soup = BeautifulSoup(imgs_, 'html.parser')
    urls = set()  # 设置一个可以去除重复字符串的列表
    # 找出所有的img标签
    for url in soup.find_all('img', attrs={}):
        try:  # 防止src标签不存在
            # url为bs4.element.Tag属性,其内部存储的标签默认形式是字典
            url = url['src']  # 获取src键内的值
            # compile函数用于预编译正则表达式，生成pattern对象，以便进行多次匹配
            absolute_url = r'((http|https|ftp)://)?(\w+)(\.\w+)+'
            absolute_url_pattern = re.compile(absolute_url, re.IGNORECASE)
            # 进行匹配
            if absolute_url_pattern.match(url):
                urls.add(url)  # 匹配成功就加入到urls列表中
                continue
        except:
            continue
    return urls


# 下载图片并保存到本地文件夹中
def download_img(links, img_path):
    for link in links:
        # 下载图片链接地址中的内容并保存到本地文件夹中
        urllib.request.urlretrieve(link, filename=img_path + '%s.jpg' % link[-8:-5])
        print('download success')


# 显示下载的图片
def show(save_paths):
    os.chdir(save_paths)
    for i in os.listdir(os.getcwd()):
        img = Image.open(i)
        img.show()


if __name__ == '__main__':
    os.chdir('/home/boni/Desktop/practice_013/')
    url = 'http://tieba.baidu.com/p/2166231880'
    save_path = '/home/boni/Desktop/practice_013/picture/'
    img_ = get_html_text(url)
    links_ = get_link_img(img_)
    download_img(links_, save_path)
    show(save_path)
