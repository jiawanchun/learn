#coding=utf-8
import unittest
from public.common import pyselenium
from config import globalparam
from public.common.log import Log

class MyTest(unittest.TestCase):
	"""
	基于所有测试用例的测试类
	"""
	@classmethod
	def setUpClass(cls):
		cls.logger = Log()
		cls.logger.info('############################### START ###############################')
		cls.dr = pyselenium.PySelenium(globalparam.browser)
		cls.dr.max_window()
		# cls.dr.open(globalparam.basurl)


	@classmethod
	def tearDownClass(cls):
		cls.dr.quit()
		cls.logger.info('###############################  End  ###############################')
	"""
	def tearDown(self):
		self.dr.F5()
	"""

