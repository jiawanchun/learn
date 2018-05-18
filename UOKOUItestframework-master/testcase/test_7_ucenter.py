#coding=utf-8
import unittest
from public.common import pyselenium
from config import globalparam
from public.common.log import Log
from public.pages import loginpage
from public.pages import ucenterpage
from time import sleep
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

@unittest.skip ("直接跳过该测试类")
class TestUokoUcenter(unittest.TestCase):
	"""优客逸家个人中心测试"""
	@classmethod
	def setUpClass(cls):
		cls.logger = Log()
		cls.logger.info('############################### START ###############################')
		cls.dr = pyselenium.PySelenium(globalparam.browser)
		cls.dr.max_window()
		uokologinpage = loginpage.LoginPage(cls.dr)
		uokologinpage.login('13408631121', '123456')
		uokologinpage.click_ucenter()

	def test_1_contracts(self):
		'''合同详情查看'''
		uokoucenterpage = ucenterpage.UcenterPage(self.dr)
		# uokoucenterpage.click_ucenter()
		uokoucenterpage.click_contracts()
		uokoucenterpage.click_view_contracts()
		sleep(3)
		self.assertIn('合同详情', uokoucenterpage.return_title())


	def test_2_myuoko_service(self):
		"""我的服务测试"""
		uokoucenterpage = ucenterpage.UcenterPage(self.dr)
		uokoucenterpage.click_myuoko_service()
		sleep(3)
		self.assertIn('我的服务', uokoucenterpage.return_title())
		# uokoucenterpage.click_view_contracts()
		# self.assertIn('服务详情', uokoucenterpage.return_title())

	def test_3_repair(self):
		"""提交维修申请测试"""
		uokoucenterpage = ucenterpage.UcenterPage(self.dr)
		uokoucenterpage.click_repair()
		# uokoucenterpage.select_room()
		uokoucenterpage.select_repair_area()
		uokoucenterpage.select_repair_option()
		#uokoucenterpage.upload_repair_picture()
		sleep(5)
		uokoucenterpage.input_repair_desc(u'子衡自动化测试维修申请')
		uokoucenterpage.sumbit_service()
		sleep(5)
		self.assertIn('我的服务', uokoucenterpage.return_title())

	def test_4_add_service(self):
		"""新增上门服务测试"""
		uokoucenterpage = ucenterpage.UcenterPage(self.dr)
		uokoucenterpage.click_workorder_service()
		# uokoucenterpage.select_room()
		uokoucenterpage.select_service_option()
		uokoucenterpage.input_desc(u'子衡自动化测试新增上门服务')
		uokoucenterpage.sumbit_service()
		sleep(10)
		self.assertIn('我的服务', uokoucenterpage.return_title())

	def test_5_complain(self):
		"""新增投诉建议测试"""
		uokoucenterpage = ucenterpage.UcenterPage(self.dr)
		uokoucenterpage.click_complain()
		# uokoucenterpage.select_room()
		uokoucenterpage.select_complain_option()
		sleep(8)
		uokoucenterpage.input_desc(u'子衡自动化测试投诉建议')
		uokoucenterpage.sumbit_service()
		sleep(2)
		self.assertIn('我的服务', uokoucenterpage.return_title())		

	def test_6_profile(self):
		"""个人资料测试"""
		uokoucenterpage = ucenterpage.UcenterPage(self.dr)
		uokoucenterpage.click_profile()

	def test_7_account_setting(self):
		"""账户设置测试"""
		uokoucenterpage = ucenterpage.UcenterPage(self.dr)
		uokoucenterpage.click_account_setting()

	def test_8_account_bill_1(self):
		"""交易详情测试"""
		uokoucenterpage = ucenterpage.UcenterPage(self.dr)
		uokoucenterpage.click_account_bill()
		uokoucenterpage.click_bill_detail()
		self.assertIn('交易详情', uokoucenterpage.return_title())

	def test_8_account_bill_2(self):
		"""收银台支付测试"""
		uokoucenterpage = ucenterpage.UcenterPage(self.dr)
		uokoucenterpage.click_account_bill()
		h = uokoucenterpage.current_window()
		uokoucenterpage.click_go_pay()
		uokoucenterpage.into_new_window()
		self.assertIn('收银台', uokoucenterpage.return_title())
		uokoucenterpage.select_pay()
		uokoucenterpage.click_pay()
		sleep(8)
		uokoucenterpage.close()
		uokoucenterpage.switch_to_window(h)

	def test_8_account_bill_3(self):
		"""合并付款测试"""
		uokoucenterpage = ucenterpage.UcenterPage(self.dr)
		uokoucenterpage.click_account_bill()
		uokoucenterpage.click_all()
		uokoucenterpage.click_batch_pay()
		sleep(2)
		self.assertIn('收银台', uokoucenterpage.return_title())
		uokoucenterpage.back()

	def test_8_account_bill_4(self):
		"""我的账单翻页测试"""
		uokoucenterpage = ucenterpage.UcenterPage(self.dr)
		uokoucenterpage.click_account_bill()
		uokoucenterpage.go_bill_pages()
		sleep(2)
		# print uokoucenterpage.go_current_page()
		self.assertEqual("4",uokoucenterpage.go_current_page())

	@classmethod
	def tearDownClass(cls):
		cls.dr.quit()
		cls.logger.info('###############################  End  ###############################')