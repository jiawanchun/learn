# coding=utf-8
from time import sleep
from public.common import mytest
from public.pages import homepage
class TestUokoHome(mytest.MyTest):
	"""优客逸家首页测试"""

	# 切换城市
	def test_1_city_list(self):
		uokohomepage = homepage.HomePage(self.dr)
		uokohomepage.open_uoko_home()
		uokohomepage.click_city_list()
		sleep(1)
		self.assertIn('http://beijing.pre.uoko.com/', uokohomepage.return_current_url())
		uokohomepage.open_cduoko_home()
	# 我要租房
	def test_2_room(self):
		uokohomepage = homepage.HomePage(self.dr)
		uokohomepage.open_uoko_home()
		uokohomepage.room()
		sleep(1)
		try:
			assert '我要租房' in uokohomepage.return_title()
			print('Test Pass.')
		except Exception as e:
			print('Test Fail.', format(e))

	# 租前须知
	def test_3_questions(self):
		uokohomepage = homepage.HomePage(self.dr)
		uokohomepage.open_uoko_home()
		sleep(1)
		try:
			assert '租前须知' in uokohomepage.questions()
			print('Test Pass.')
		except Exception as e:
			print('Test Fail.', format(e))

	# 房东加盟
	def test_4_fd(self):
		uokohomepage = homepage.HomePage(self.dr)
		uokohomepage.open_uoko_home()
		sleep(1)
		try:
			assert '优客逸家-房屋托管公司' in uokohomepage.fd()
			print('Test Pass.')
		except Exception as e:
			print('Test Fail.', format(e))

	# 关于优客
	def test_5_about(self):
		uokohomepage = homepage.HomePage(self.dr)
		uokohomepage.open_uoko_home()
		sleep(1)
		try:
			assert '关于优客' in uokohomepage.about()
			print('Test Pass.')
		except Exception as e:
			print('Test Fail.', format(e))

	# 首页搜索
	def test_6_home_search(self):
		uokohomepage = homepage.HomePage(self.dr)
		uokohomepage.open_uoko_home()
		uokohomepage.home_search_key(u'光明城市')
		uokohomepage.click_search_button()
		sleep(2)
		try:
			assert u'光明城市' in uokohomepage.return_title()
			print('Test Pass.')
		except Exception as e:
			print('Test Fail.', format(e))

	# 热门区域
	def test_7_hot_area(self):
		hotareaurllist = [u'http://www.pre.uoko.com/room/pg1/_布鲁明顿', u'http://www.pre.uoko.com/room/pg1/_金牛区',
						u'http://www.pre.uoko.com/room/pg1/_武侯区', u'http://www.pre.uoko.com/room/pg1/_九里堤',
						u'http://www.pre.uoko.com/room/pg1/_内光华', u'http://www.pre.uoko.com/room/pg1/_红牌楼']
		uokohomepage = homepage.HomePage(self.dr)
		uokohomepage.open_uoko_home()
		uokohomepage.hot_area()
		sleep(2)
		# self.assertIn(uokohomepage.return_current_url(), hotareaurllist)
		try:
			assert uokohomepage.return_current_url() in hotareaurllist
			print('Test Pass.')
		except Exception as e:
			print('Test Fail.', format(e))

	# 首页地图找房
	def test_8_home_map(self):
		uokohomepage = homepage.HomePage(self.dr)
		uokohomepage.open_uoko_home()
		uokohomepage.click_map_search()
		sleep(2)
		self.assertIn('room/map', uokohomepage.return_current_url())

	# 首页房源链接点击
	def test_9_home_room(self):
		uokohomepage = homepage.HomePage(self.dr)
		uokohomepage.open_uoko_home()
		h=uokohomepage.current_window()
		uokohomepage.click_home_house()
		sleep(2)
		uokohomepage.into_new_window()
		print uokohomepage.return_current_url()
		self.assertIn('room', uokohomepage.return_current_url())
		uokohomepage.close()
		uokohomepage.switch_to_window(h)


	"""
	# 首页企业客户入口
	def test_corporate(self):
		uokohomepage = homepage.HomePage(self.dr)
		uokohomepage.open_uoko_home()
		uokohomepage.click_corporate_entrance()
		sleep(2)
		self.assertIn('/special/corporate/', uokohomepage.return_current_url())
	"""



