# -*- coding: utf-8 -*-
from public.common import basepage
from time import sleep
class RoomDetailsPage(basepage.Page):
	# 进入房间详情
	def open_room_detail(self):
		self.dr.open('http://www.pre.uoko.com/room/37618e979be94bad9219c0aece07d532')
	# 点击某一个房间 a-e 为1-5
	def click_one_house(self):
		self.dr.click("xpath->.//*[@id='state-label-group']/div[1]")
	# 点击我要看房
	def click_see_house(self):
		self.dr.click("xpath->.//*[@id='look-link-old']")
	# 输入你的名字
	def input_your_name(self,values):
		self.dr.type('name->name',values)
	# 输入你的手机
	def input_your_phone(self,values):
		self.dr.type('name->phone',values)
	# 选择性别
	def select_gender(self):
		# self.dr.type('class->gender',values)
		self.dr.click("xpath->.//*[@id='reserveForm']/div[1]/div[3]/div/label[2]/input")  #点击女
	# 选择入住人数
	def select_peoplenumber(self):
		self.dr.click("xpath->//*[@id='reserveForm']/div[1]/div[4]/div/label[2]")  # 点击男
	# 选择预约时间 2017-09-27 14:00
	def select_book_time(self, values):
		self.dr.type('id->datetime_plan', values)
	# 输入个人需求
	def input_personal_needs(self, values):
		self.dr.type("xpath->.//*[@id='reserveForm']/div[1]/div[6]/div/textarea", values)
	# 点击提交按钮
	def click_submit_reserveroom(self):
		self.dr.click('id->reserveRoom')
	# 预约成功文本信息
	def reserver_sucess_text(self):
		return self.dr.get_text("xpath->.//*[@id='order-modal-callback']/div/div[1]/p/b/span")
	# 猜你喜欢
	def guess_you_like(self):
		js = "var q=document.documentElement.scrollTop=10000"
		self.dr.js(js)
		self.dr.click("xpath->.//*[@id='item-info-verbose']/div[1]/div[7]/div[2]/ul/li[1]/p[1]/a")
	# 房间标题
	def house_loc_name(self):
		return  self.dr.get_text('id->loc-name')
	# 附近热租房源
	def click_hot_house(self):
		self.dr.js("window.scrollBy(0,400)")
		# hot_list = self.dr.origin_driver.find_elements_by_css_selector("#hot-list a")
		hot_list = self.dr.get_elements('css->.hot-list>.desc>a')
		hoturllist =[]
		baseurl ='http://www.pre.uoko.com'
		for hot in hot_list:
			hoturl = hot.get_attribute("href")
			print hoturl
			hoturllist.append(hoturl)
		for hot in hoturllist:
			url= baseurl + hot
			print url
			self.dr.open(url)
			sleep(5)

		# self.dr.click("xpath->.//*[@id='item-info-verbose']/div[2]/div[2]/ul/li[2]/p[1]/a")

	# 客服咨询
	def click_custom_service(self):
		self.dr.click('id->QQMessageOnlick')
	# 聊天窗口标题
	def chat_header_name(self):
		return self.dr.get_text('class->chat-header-name')
	# 关闭聊天窗口
	def click_close_chat(self):
		self.dr.click('class->ntalk-button-close')


	def return_title(self):
		return self.dr.get_title()
	def return_url(self):
		return self.dr.get_url()

