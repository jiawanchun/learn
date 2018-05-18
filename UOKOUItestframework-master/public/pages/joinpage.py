# -*- coding: utf-8 -*-
from public.common import basepage
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import UnexpectedAlertPresentException
class JoinPage(basepage.Page):
	# 打开优客逸家首页
	def open_uoko_home(self):
		self.dr.open('http://www.pre.uoko.com')
	# 点击注册按钮
	def click_join_button(self):
		self.dr.click_text('注册')
	# 输入手机号 随机产生手机号
	def input_phone(self,values):
		self.dr.type('id->Phone',values )
	# 设置密码
	def set_password(self,values):
		self.dr.clear_type('id->password', values)
	# 确认密码
	def confirm_password(self,values):
		self.dr.clear_type('name->passwordAgain', values)
	# 拖动滑块 发送验证码
	def drage_slider(self):
		# dragger = self.dr.get_element('class->slider-thumb js-thumb roll-back')
		dragger = self.dr.origin_driver.find_element_by_xpath(".//*[@id='slider-bar']/div[1]")
		action = ActionChains(self.dr.origin_driver)
		action.click_and_hold(dragger).perform()        # 鼠标左键按下不放
		for index in range(7):
			try:
				action.move_by_offset(50, 0).perform()    # 平行移动鼠标
			except UnexpectedAlertPresentException:
				break
			sleep(0.05)  # 等待停顿时间
		# success_text = self.dr.origin_driver.switch_to.alert.text
		# print success_text
	# 输入验证码
	def input_smscode(self,values):
		self.dr.type('id->verifyCode',values)
	# 点击注册按钮
	def submit_join_button(self):
		# self.dr.click('class->sub-btn')
		self.dr.origin_driver.find_element_by_class_name('sub-btn').submit()
	# 获取注册成功信息
	def join_success_text(self):
		return self.dr.get_text("xpath->.//*[@id='modal-reg-succ']/div/div/h3")
	# 点击立即租房按钮
	def click_room(self):
		self.dr.click('class->go-home-btn')

	def return_title(self):
		return self.dr.get_title()
	def return_url(self):
		return self.dr.get_url()
	def accept_alert(self):
		self.dr.origin_driver.switch_to_alert().accept()
	def alert_text(self):
		text = self.dr.origin_driver.switch_to_alert().text
		return text

	def join_page_source(self):
		return self.dr.origin_driver.page_source











