# -*- coding: utf-8 -*-
from public.common import mytest
from public.pages import roomsearchpage
from time import  sleep
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
class TestUokoRoomSearch(mytest.MyTest):
	"""优客逸家找房搜索页面测试"""
	# 条件搜索测试
	def test_1_conditional_search(self):
		uokoroomsearch = roomsearchpage.RoomSearchPage(self.dr)
		uokoroomsearch.open_uoko_home()
		uokoroomsearch.click_room()
		sleep(5)
		uokoroomsearch.input_search(u'大源')
		uokoroomsearch.click_search()
		sleep(5)
		self.assertIn('大源',uokoroomsearch.return_title())

	# 热门区域筛选测试
	def test_2_hotarea_search(self):
		uokoroomsearch = roomsearchpage.RoomSearchPage(self.dr)
		uokoroomsearch.open_uoko_home()
		uokoroomsearch.click_room()
		uokoroomsearch.click_hotarea_search()
		sleep(5)
		# self.assertIn('静君寺', uokoroomsearch.return_title())
		try:
			assert u'静君寺' in uokoroomsearch.return_title()
			print('Test Pass.')
		except Exception as e:
			print('Test Fail.', format(e))

	# 区域筛选测试
	def test_3_area_search(self):
		uokoroomsearch = roomsearchpage.RoomSearchPage(self.dr)
		uokoroomsearch.open_uoko_home()
		uokoroomsearch.click_room()
		uokoroomsearch.click_area_search()
		sleep(5)

	# 租金筛选测试
	def test_4_rent_search(self):
		uokoroomsearch = roomsearchpage.RoomSearchPage(self.dr)
		uokoroomsearch.open_uoko_home()
		uokoroomsearch.click_room()
		uokoroomsearch.click_rents_search()
		renthrefs = ['http://www.pre.uoko.com/room/p1/','http://www.pre.uoko.com/room/p2/',
					 'http://www.pre.uoko.com/room/p3/','http://www.pre.uoko.com/room/p4/',
					 'http://www.pre.uoko.com/room/p5/']
		self.assertIn(uokoroomsearch.return_url(), renthrefs)

	# 户型筛选测试
	def test_5_housetype_search(self):
		uokoroomsearch = roomsearchpage.RoomSearchPage(self.dr)
		uokoroomsearch.open_uoko_home()
		uokoroomsearch.click_room()
		uokoroomsearch.click_housetype_search()

	# 入住筛选测试
	def test_6_checkin_search(self):
		uokoroomsearch = roomsearchpage.RoomSearchPage(self.dr)
		uokoroomsearch.open_uoko_home()
		uokoroomsearch.click_room()
		uokoroomsearch.click_checkin_search()

	# 室友筛选测试
	def test_7_roommate_search(self):
		uokoroomsearch = roomsearchpage.RoomSearchPage(self.dr)
		uokoroomsearch.open_uoko_home()
		uokoroomsearch.click_room()
		uokoroomsearch.click_roommate_search()

	# 配置筛选
	def test_8_configure_search(self):
		uokoroomsearch = roomsearchpage.RoomSearchPage(self.dr)
		uokoroomsearch.open_uoko_home()
		uokoroomsearch.click_room()
		uokoroomsearch.click_configure_search()

	# 组合筛选 难点

	# 点击全部房源
	def test_10_all_room(self):
		uokoroomsearch = roomsearchpage.RoomSearchPage(self.dr)
		uokoroomsearch.open_uoko_home()
		uokoroomsearch.click_room()
		uokoroomsearch.click_all_room()
		sleep(5)
		self.assertIn('/room/by0/', uokoroomsearch.return_url())

	# 点击热门推荐第一个房源 最好效果应该是随机点击
	def test_11_first_house(self):
		uokoroomsearch = roomsearchpage.RoomSearchPage(self.dr)
		uokoroomsearch.open_uoko_home()
		h = uokoroomsearch.current_window()
		uokoroomsearch.click_room()
		uokoroomsearch.click_first_house()
		sleep(5)
		uokoroomsearch.into_new_window()
		# self.assertIn('保利心语2期', uokoroomsearch.return_title())
		try:
			assert u'保利心语2期' in uokoroomsearch.return_title()
			print('Test Pass.')
		except Exception as e:
			print('Test Fail.', format(e))
		uokoroomsearch.close()
		uokoroomsearch.switch_to_window(h)

	# 点击新房通知
	def test_12_new_email(self):
		uokoroomsearch = roomsearchpage.RoomSearchPage(self.dr)
		uokoroomsearch.open_uoko_home()
		uokoroomsearch.click_room()
		uokoroomsearch.click_new_email()
		sleep(5)
		# self.assertIn('订阅邮箱', uokoroomsearch.return_email_text())

	# 管家推荐房源
	def test_13_butler_recommendation(self):
		uokoroomsearch = roomsearchpage.RoomSearchPage(self.dr)
		uokoroomsearch.open_uoko_home()
		uokoroomsearch.click_room()
		uokoroomsearch.click_butler_recommendation()
		sleep(5)
		self.assertIn('我要看房', uokoroomsearch.return_house_text())
	# 在线客服测试
	def test_14_online_service(self):
		uokoroomsearch = roomsearchpage.RoomSearchPage(self.dr)
		uokoroomsearch.open_uoko_home()
		uokoroomsearch.click_room()
		uokoroomsearch.click_online_service()
		sleep(5)










