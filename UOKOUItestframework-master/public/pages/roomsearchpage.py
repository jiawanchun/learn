# -*- coding: utf-8 -*-
from public.common import basepage
from time import sleep
class RoomSearchPage(basepage.Page):
	# 打开优客逸家首页
	def open_uoko_home(self):
		self.dr.open('http://www.pre.uoko.com')
	# 点击我要租房
	def click_room(self):
		self.dr.click_text('我要租房')
	# 点击地图找房
	def click_map_search(self):
		self.dr.click('class->hd-item by-map')

	# 条件搜索框搜房
	def input_search(self, values):
		self.dr.type('id->search-ipt',values)
	# 点击搜索按钮
	def click_search(self):
		self.dr.click("xpath->.//*[@id='page-main']/div[3]/div/div/div[2]/div[1]/div[1]/form/input[2]")
	# 热门区域搜索
	def click_hotareas_search(self):
		self.dr.get_elements("class->hot-words")
		"""
		for hotarea in hotareas:
			self.dr.click(hotarea)
			sleep(5)
		"""
	# 点击热门区域的某一个区域进行搜索  如 金牛区
	def click_hotarea_search(self):
		self.dr.click("xpath->.//*[@id='page-main']/div[3]/div/div/div[2]/div[1]/div[2]/a[2]")

	# 区域筛选
	def click_area_search(self):
		self.dr.click("xpath->.//*[@id='page-main']/div[3]/div/div/div[2]/div[2]/div[1]/div/a[2]")

	# 租金筛选
	def click_rents_search(self):
		rents = ['500-700','700-1000','1000-1500','1500-2000','2000以上']
		for rent in rents:
			self.dr.click_text(rent)
			sleep(5)
	def click_rent_search(self):
		self.dr.click_text('500-700')

	# 户型筛选
	def click_housetype_search(self):
		housetypes = ['普通单间','主卧带独卫','标间小套一','整租']
		for housetype in housetypes:
			self.dr.click_text(housetype)
			sleep(5)

	# 入住筛选
	def click_checkin_search(self):
		checkins = ['可立即入住','一周内可入住','两周内可入住']
		for checkin in checkins:
			self.dr.click_text(checkin)
			sleep(5)

	# 室友筛选
	def click_roommate_search(self):
		roommates = ['无所谓','全是妹子','全是汉子','爱情公寓']
		for roommate in roommates:
			self.dr.click_text(roommate)
			sleep(5)

	# 配置筛选
	def click_configure_search(self):
		# configures = ['独立卫生间','带阳台','带飘窗','可住两人']
		configures =['http://www.pre.uoko.com/room/a1/','http://www.pre.uoko.com/room/a3/',
						'http://www.pre.uoko.com/room/a7/','http://www.pre.uoko.com/room/a15/']

		for configure in configures:
			# self.dr.click_text(configure)
			self.dr.open(configure)
			sleep(5)

	# 全部房源
	def click_all_room(self):
		self.dr.click("xpath->.//*[@id='page-main']/div[4]/div/div/a[2]")

	# 热门推荐第一个房源  （以后要做成随机点击）
	def click_first_house(self):
		self.dr.js("window.scrollBy(0,300)")  #往下拉
		self.dr.click("xpath->.//*[@id='page-main']/div[4]/div/ul/li[1]/div[2]/a")

	# 新房通知
	def click_new_email(self):
		self.dr.click("xpath->.//*[@id='page-main']/div[4]/div/div/a[2]")
		# self.dr.origin_driver.find_element_by_xpath("xpath->.//*[@id='page-main']/div[4]/div/div/a[2]").click()
	def return_email_text(self):
		return self.dr.get_text("xpath->.//*[@id='page-main']/div[2]/ol/li[2]")

	# 点击在线客服
	def click_online_service(self):
		self.dr.click('id->customer-service-img')

	# 点击管家推荐  随机选择
	def click_butler_recommendation(self):
		self.dr.js("window.scrollBy(0,10000)")           # 滚到底部
		self.dr.click("xpath->.//*[@id='AsyncLoading']/ul/li[1]/p[1]/a")

	def return_house_text(self):
		return self.dr.get_text("xpath->.//*[@id='look-link-old']")

	def return_title(self):
		return self.dr.get_title()
	def return_url(self):
		return self.dr.get_url()

	# 窗口相关操作
	def close(self):
		self.dr.close()
	def new_window(self):
		self.dr.open_new_window()
	def into_new_window(self):
		self.dr.into_new_window()
	def current_window(self):
		return self.dr.origin_driver.current_window_handle
	def all_windows(self):
		return self.dr.origin_dirver.window_handles
	def switch_to_window(self,values):
		self.dr.origin_driver.switch_to_window(values)


