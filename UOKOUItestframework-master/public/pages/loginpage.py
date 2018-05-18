# coding:utf-8
from public.common import basepage
class LoginPage(basepage.Page):

	# 打开优客逸家首页
	def open_uoko_home(self):
		self.dr.open('http://www.pre.uoko.com')
	# 点击登录按钮
	def click_login_button(self):
		self.dr.click_text('登录')

	# 输入用户名
	def input_username(self, values):
		self.dr.clear_type('id->username',values)

	# 输入密码
	def input_password(self, values):
		self.dr.clear_type('name->password', values)

	# 点击登录按钮
	def click_logButton (self):
		self.dr.click('class->sub-btn')

	# 登录后的昵称
	def login_nickname(self):
		nickname = self.dr.get_text("xpath->.//*[@id='page-main']/div[1]/div/div[3]/span/a")
		return nickname
		#return self.dr.js('var p_text =$(".uoko-navbar-right a").text(); alert(p_text);')
	# 登录按钮
	def login_button_text(self):
		return self.dr.get_text("xpath->.//*[@id='page-main']/div[1]/div/div[3]/a[1]")

	# 进入个人中心
	def click_ucenter(self):
		self.dr.click("xpath->.//*[@id='page-main']/div[1]/div/div[3]/span/a")
	# 点击退出按钮
	def logout(self):
		self.dr.click_text('退出')
	# 登录错误提示信息
	def login_error_msg(self):
		return self.dr.get_text('id->server-error-box')

	def login(self, username,psw):
		"""登录公共方法"""
		self.open_uoko_home()
		self.click_login_button()
		self.input_username(username)
		self.input_password(psw)
		self.click_logButton()


