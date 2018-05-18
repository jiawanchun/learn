# coding=utf-8
from time import sleep
from public.common import mytest
from public.pages import roomdetailspage
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
class TestUokoRoomdetails(mytest.MyTest):
	"""优客逸家房源详情页测试"""

	# 点击进入房源详情页
	def test_1_open_roomdetails(self):
		uokoroomdetailspage = roomdetailspage.RoomDetailsPage(self.dr)
		uokoroomdetailspage.open_room_detail()
		sleep(5)
		self.assertIn('软件园 三利宅院旁', uokoroomdetailspage.return_title())

	# 预约看房测试
	def test_2_reserveroom(self):
		text = u'子衡自动化测试信息'
		# text2 = unicode("子衡自动化测试信息").encode("utf-8")
		uokoroomdetailspage = roomdetailspage.RoomDetailsPage(self.dr)
		uokoroomdetailspage.open_room_detail()
		sleep(5)
		uokoroomdetailspage.click_one_house()
		uokoroomdetailspage.click_see_house()
		uokoroomdetailspage.input_your_name('zihengtest')
		uokoroomdetailspage.input_your_phone('18200201037')
		uokoroomdetailspage.select_gender()
		uokoroomdetailspage.select_peoplenumber()
		uokoroomdetailspage.select_book_time('2017-09-27 14:00')
		uokoroomdetailspage.input_personal_needs(text)
		sleep(5)
		uokoroomdetailspage.click_submit_reserveroom()
		sleep(2)
		print uokoroomdetailspage.reserver_sucess_text()
		# self.assertIn('zihengtest先生',uokoroomdetailspage.reserver_sucess_text())
		try:
			assert u'zihengtest先生' in uokoroomdetailspage.reserver_sucess_text()
			print('Test Pass.')
		except Exception as e:
			print('Test Fail.', format(e))

	# 猜你喜欢测试
	def test_3_guessyoulike(self):
		uokoroomdetailspage = roomdetailspage.RoomDetailsPage(self.dr)
		uokoroomdetailspage.open_room_detail()
		uokoroomdetailspage.guess_you_like()
		sleep(2)
		self.assertIn('中德英伦联邦C区',uokoroomdetailspage.house_loc_name())

	# 附近热租房源测试
	def test_4_hot_house(self):
		uokoroomdetailspage = roomdetailspage.RoomDetailsPage(self.dr)
		uokoroomdetailspage.open_room_detail()
		uokoroomdetailspage.click_hot_house()
		sleep(2)
		# self.assertIn('领馆国际城', uokoroomdetailspage.house_loc_name())

	# 客服咨询
	def test_5_custom_service(self):
		uokoroomdetailspage = roomdetailspage.RoomDetailsPage(self.dr)
		uokoroomdetailspage.open_room_detail()
		uokoroomdetailspage.click_custom_service()
		sleep(2)
		print uokoroomdetailspage.chat_header_name()
		self.assertIn(u'优客家妹儿' ,uokoroomdetailspage.chat_header_name())
		uokoroomdetailspage.click_close_chat()

