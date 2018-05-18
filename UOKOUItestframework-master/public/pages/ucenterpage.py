# -*- coding: utf-8 -*-
from public.common import basepage
from selenium.webdriver.support.select import Select
from time import sleep
from random import choice
import re
import os
import SendKeys

class UcenterPage(basepage.Page):

	# 进入个人中心
	def click_ucenter(self):
		self.dr.click("xpath->.//*[@id='page-main']/div[1]/div/div[3]/span/a")

	# 点击我的合同
	def click_contracts(self):
		self.dr.click_text('我的合同')
	# 点击查看合同
	def click_view_contracts(self):
		self.dr.click("xpath->.//*[@id='page-main']/div[2]/div/table/tbody/tr[1]/td[6]/a")

	"""服务"""
	# 点击我的服务
	def click_myuoko_service(self):
		self.dr.click_text('我的服务')
	# 点击查看详情
	def clcik_view_detail(self):
		self.dr.click("xpath->.//*[@id='page-main']/div[2]/div/section/div/div[1]/div[2]/a")

	# 点击维修申请
	def click_repair(self):
		self.dr.click_text('维修申请')
	# 选择维修区域 如我的房间
	def select_repair_area(self):
		sel = self.dr.origin_driver.find_element_by_id('RoomName')
		Select(sel).select_by_index('1')
	# 选择维修项
	def select_repair_option(self):
		self.dr.click("xpath->.//*[@id='typeinfo']/li/ul/li[1]/label")
		self.dr.click("xpath->.//*[@id='typeinfo']/li[2]/ul/li[2]/label")

	# 上传维修照片
	def upload_repair_picture(self):
		# 打开上传按钮
		self.dr.click('id->browse')
		sleep(10)
		# os.system(r'D:\ziheng\autoitscrite\upload.exe')
		SendKeys.SendKeys('D:\\ziheng\\test\\01.jpg') #发送图片地址
		SendKeys.SendKeys("{ENTER}")                #发送回车键

	# 填写维修描述
	def input_repair_desc(self, values):
		self.dr.type('id->RepairMsg', values)

	# 点击上门服务
	def click_workorder_service(self):
		self.dr.click_text('上门服务')
	def select_room(self):
		# 选择服务房间
		sel = self.dr.origin_driver.find_element_by_xpath(".//*[@id='formaddress']")
		Select(sel).select_by_index('1')
		#选择服务
	def select_service_option(self):
		self.dr.click("xpath->.//*[@id='serviceForm']/div[2]/div/a[1]")  # 选择服务选项 如看房
		#填入服务描述   #共用
	def input_desc(self,values):
		self.dr.type('id->ServiceMsg', values)


	# 点击投诉建议
	def click_complain(self):
		self.dr.click_text('投诉建议')
	# 选择投诉房源  跟上门服务一样的 可以不写
	def select_complain_room(self):  #共用
		sel = self.dr.origin_driver.find_element_by_xpath(".//*[@id='formaddress']")
		Select(sel).select_by_index('2')
	# 选择投诉项
	def select_complain_option(self):
		"""
		options = self.dr.origin_driver.find_elements_by_css_selector('# service-rent>a')
		choice(options).click()
		"""
		self.dr.click("xpath->.//*[@id='complainForm']/div[3]/div/a[1]")
	# 点击确认提交
	def sumbit_service(self):   #共用
		self.dr.click('id->btnSave')



	"""账户"""
	# 点击个人资料
	def click_profile(self):
		self.dr.click_text('个人资料')


	# 账户设置
	def click_account_setting(self):
		self.dr.click_text('账户设置')


	# 我的账单
	def click_account_bill(self):
		self.dr.click_text('我的账单')
	# 点击第一个账单立即付款
	def click_go_pay(self):
		self.dr.click("xpath->.//*[@id='acc-table-bd']/tr[1]/td[6]/a[1]")
	# 选择微信支付
	def select_pay(self):
		self.dr.click("xpath->html/body/div[2]/div/div[4]/div/div[2]/label/input")
	# 点击立即支付
	def click_pay(self):
		self.dr.click("xpath->.//*[@id='payform']/div/div[2]/input[1]")

	# 点击第一个账单详情查看
	def click_bill_detail(self):
		self.dr.click("xpath->.//*[@id='acc-table-bd']/tr[1]/td[6]/a[2]")
	# 点击全选按钮
	def click_all(self):
		self.dr.click('class->theme-checkbox')
	# 点击合并付款
	def click_batch_pay(self):
		self.dr.click('name->batchpaybtn')


	# 我的账单页面
	def go_bill_pages(self):
		"""
		total_pages = len(self.dr.origin_driver.find_element_by_class_name("pagination").
		                  find_elements_by_tag_name("li")) - 2
		print "total_pages is %s" % total_pages
		"""
		# 跳转到第二页
		self.dr.js("window.scrollBy(0,9000)")
		next_page = self.dr.origin_driver.find_element_by_class_name("pagination").find_element_by_link_text("4")
		next_page.click()
	def go_current_page(self):
		# 获取当前页面是第几页
		current_page = self.dr.origin_driver.find_element_by_class_name('pagination').find_element_by_class_name('on')
		return current_page.text
		# print "current page is %s" %  current_page.text

		
		

	# 返回标题
	def return_title(self):
		return self.dr.get_title()
	def return_url(self):
		return self.dr.get_url()
	# 返回上一页
	def back(self):
		self.dr.origin_driver.back()
	# 窗口相关操作
	def close(self):
		self.dr.close()
	def into_new_window(self):
		self.dr.into_new_window()
	def current_window(self):
		return self.dr.origin_driver.current_window_handle
	def all_windows(self):
		return self.dr.origin_dirver.window_handles
	def switch_to_window(self,values):
		self.dr.origin_driver.switch_to_window(values)







