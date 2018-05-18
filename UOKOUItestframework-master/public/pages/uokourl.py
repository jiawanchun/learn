# coding:utf-8
# 链接 http://www.cnblogs.com/helenMemery/p/6543030.html
import re,requests
from selenium import webdriver
from public.common import basepage
# 爬取网页资源，并用正则表达式匹配出URL
class UokoLink(basepage.Page):
	def get_urlList(self, values):
		self.dr.open(values)
		# 获取网页资源
		page = self.dr.origin_driver.page_source
		# 用正则表达式匹配URL集
		url_context = re.findall('href=\"(.*?)\"',page,re.S)
		url_list = []
		for url in url_context:
			# 因为url_context中匹配的内容有些不是URL，所以加个if来过滤一下
			if 'http'in url:
				url_list.append(url)
		# 因为网页中的URL基本是正确的，下面我们可以加入一个不存在的URL，检查异常URL的输出
		url_list.append('http://www.pre.uoko.com/room/456')
		return url_list

	# 通过request.get检查URL的返回编码状态，以确认URL返回正常
