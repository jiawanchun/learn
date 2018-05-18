#coding=utf-8
import unittest
from public.common import pyselenium
from config import globalparam
from public.common.log import Log
from public.pages import homepage
from public.pages import mapsearchpage
from time import sleep
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class TestUokoUcenter(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.logger = Log()
		cls.logger.info('############################### START ###############################')
		cls.dr = pyselenium.PySelenium(globalparam.browser)
		cls.dr.max_window()
		uokohomepage = homepage.HomePage(cls.dr)
		uokohomepage.open_uoko_home()
		uokohomepage.click_map_search()
		uokohomepage.zoomin_js()
		sleep(5)
	def test_1_input_search(self):
		uokomapsearchpage = mapsearchpage.MapSearchPage(self.dr)
		uokomapsearchpage.input_search(u'光明城市')  # 地图搜索怎么作断言
	def test_2_prince_search(self):
		uokomapsearchpage = mapsearchpage.MapSearchPage(self.dr)
		uokomapsearchpage.price_search()
	def test_3_housetype_search(self):
		uokomapsearchpage = mapsearchpage.MapSearchPage(self.dr)
		uokomapsearchpage.housetype_search()
	def test_4_config_search(self):
		uokomapsearchpage = mapsearchpage.MapSearchPage(self.dr)
		uokomapsearchpage.config_search()






	@classmethod
	def tearDownClass(cls):
		cls.dr.quit()
		cls.logger.info('###############################  End  ###############################')