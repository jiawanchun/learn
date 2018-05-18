# -*- coding: utf-8 -*-
from public.common import basepage
from time import sleep
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
class MapSearchPage(basepage.Page):
	# 打开优客逸家首页
	def open_uoko_home(self):
		self.dr.open('http://www.pre.uoko.com')
	# 点击地图找房
	def click_map_search(self):
		self.dr.click("xpath->.//*[@id='page-main']/div[3]/div/a")
	# 输入条件搜索
	def input_search(self, values):
		self.dr.type('id->inputName', values)
	# 价格搜索 价格700-1000
	def price_search(self):
		"""
		prices = self.dr.origin_driver.find_element_by_class_name('sel_more').find_elements_by_tag_name('li')
		for price in prices:
			price.click()
			sleep(5)
		"""
		self.dr.move_to_element("xpath->.//*[@id='page-main']/div[2]/div[1]/div[1]/div[1]/span")
		self.dr.click("xpath->.//*[@id='page-main']/div[2]/div[1]/div[1]/div[1]/ul/li[3]")
		sleep(5)
	# 户型搜索 普通单间
	def housetype_search(self):
		self.dr.move_to_element("xpath->.//*[@id='page-main']/div[2]/div[1]/div[1]/div[2]/span")
		self.dr.click("xpath->.//*[@id='page-main']/div[2]/div[1]/div[1]/div[2]/ul/li[2]")
		sleep(2)

	# 配置搜索  带飘窗
	def config_search(self):
		self.dr.move_to_element("xpath->.//*[@id='page-main']/div[2]/div[1]/div[1]/div[3]/span")
		self.dr.click("xpath->.//*[@id='page-main']/div[2]/div[1]/div[1]/div[3]/ul/li[4]")
		sleep(3)

