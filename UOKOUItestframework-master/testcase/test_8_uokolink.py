# coding=utf-8
from time import sleep
from public.common import mytest
from public.pages import uokourl
import requests
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class TestUokourl(mytest.MyTest):
	"""优客逸家链接测试"""
	def test_uokolink(self):
		target_page = 'http://www.pre.uoko.com/room/'
		uokourllink = uokourl.UokoLink(self.dr)
		url_list = uokourllink.get_urlList(target_page)
		print url_list
		for url in  url_list:
			print  url
			r = requests.get(url)
			print r.status_code
		"""
		try:
			for url in url_list:
				r = requests.get(url)
				if r.status_code !=200:
					print url
		except requests.HTTPError,e:
			e.strerror
		"""