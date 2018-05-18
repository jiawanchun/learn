# -*- coding: utf-8 -*-
from public.common import basepage
from time import sleep
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
class HomePage(basepage.Page):

	# 打开优客逸家首页
	def open_uoko_home(self):
		self.dr.open('http://www.pre.uoko.com')

	def open_cduoko_home(self):
		self.dr.open('http://chengdu.pre.uoko.com')

	# 切换城市
	def click_city_list(self):
		"""
		# citys = self.dr.origin_driver.find_elements_by_css_selector("#city-list a")
		citys = self.dr.get_elements('css->#city-list a')
		cityurllist =[]
		for city in citys:
			cityurl = city.get_attribute("href")
			cityurllist.append(cityurl)
		print cityurllist
		for city in cityurllist:
			self.dr.open(city)
			sleep(5)
		"""
		# 鼠标移动元素切换点击
		self.dr.click('class->city-selection')
		self.dr.move_to_element("xpath->.//*[@id='city-list']/li[3]/a")
		self.dr.click("xpath->.//*[@id='city-list']/li[3]/a")
		sleep(5)


	# 点击我要租房
	def room(self):
		self.dr.click_text('我要租房')

	# 点击租前须知
	def questions(self):
		self.dr.click_text('租前须知')
		return self.dr.get_title()

	# 点击房东加盟
	def fd(self):
		self.dr.click_text('房东加盟')
		return self.dr.get_title()

	# 点击关于优客
	def about(self):
		self.dr.click_text('关于优客')
		return self.dr.get_title()

	# 首页搜索关键字
	def home_search_key(self, values):
		self.dr.type('id->search-ipt', values)

	# 点击搜索按钮
	def click_search_button(self):
		self.dr.click("xpath->.//*[@id='page-main']/div[3]/div/div[1]/form/input[2]")

	# 点击地图找房
	def click_map_search(self):
		self.dr.click("xpath->.//*[@id='page-main']/div[3]/div/a")
	# 收缩页面
	def zoomin_js(self):
		self.dr.js("$('.serach_house_name').find('button').trigger('click')")
	# 热门区域
	def hot_area(self):
		hotareas = [u'布鲁明顿',u'金牛区',u'武侯区',u'九里堤',u'内光华',u'红牌楼']
		for hotarea in hotareas:
			self.dr.click_text(hotarea)
			sleep(5)

	# 企业客户入口
	def click_corporate_entrance(self):
		self.dr.js("window.scrollBy(0,8500)")
		"""
		baseurl = 'http://wwww.uoko.com'
		href = self.dr.get_attribute("xpath->.//*[@id='page-main']/div[6]/div/div[2]/a[1]/img","href")
		url =baseurl+href
		self.dr.open(url)
		"""
		self.dr.click("xpath->.//*[@id='page-main']/div[6]/div/div[2]/a[1]/img")


	# 点击房源 怎么随机点击每一个房源
	def click_home_house(self):
		self.dr.js("window.scrollBy(0,500)")
		self.dr.click("xpath->.//*[@id='page-main']/div[4]/div/ul/li[1]/div[2]/a")
		# self.dr.open_new_window("xpath->.//*[@id='page-main']/div[4]/div/ul/li[1]/div[2]/a")

	# 返回当前标题
	def return_title(self):
		return self.dr.get_title()

	# 返回当前url
	def return_current_url(self):
		return self.dr.get_url()

	#窗口相关操作
	def close(self):
		self.dr.close()
	def into_new_window(self):
		self.dr.into_new_window()
	def current_window(self):
		return self.dr.origin_driver.current_window_handle
	def all_windows(self):
		return self.dr.origin_dirver.window_handles
	def switch_to_window(self,values):
		self.dr.origin_driver.switch_to_window(values)




