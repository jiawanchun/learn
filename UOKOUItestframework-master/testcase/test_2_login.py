# coding=utf-8
from public.common import mytest
from public.pages import loginpage
from time import  sleep
class TestUokoLogin(mytest.MyTest):
	"""优客逸家登录测试"""
	def test_1_login(self):
		"""直接登录用例01"""
		uokologinpage = loginpage.LoginPage(self.dr)
		uokologinpage.login('13408631121','123456')
		sleep(2)
		self.assertEqual('zihengtest', uokologinpage.login_nickname())
		uokologinpage.logout()
		sleep(2)
		print uokologinpage.login_button_text()
		self.assertIn('登录',uokologinpage.login_button_text())
	def test_2_login(self):
		"""错误登录用例"""
		uokologinpage = loginpage.LoginPage(self.dr)
		uokologinpage.login('13408631121', '654321')
		sleep(1)
		self.dr.take_screenshot(r"E:\CI\UOKOUItestframework-master\report\img\login_password_incorrect.jpg")
		erroemsg = uokologinpage.login_error_msg()
		print erroemsg
		self.assertIn('账号或密码错误',uokologinpage.login_error_msg())







