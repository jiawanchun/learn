# -*- coding: utf-8 -*-
from time import sleep
from public.common import mytest
from public.common import publicfunction
from public.pages import joinpage

class TestUokoJoin(mytest.MyTest):
	"""优客逸家注册测试"""
	#全局变量 其余函数也可以使用
	phone = publicfunction.createphone()
	print phone
	def test_1_join(self):
		uokojoinpage = joinpage.JoinPage(self.dr)
		uokojoinpage.open_uoko_home()
		uokojoinpage.click_join_button()
		sleep(2)
		uokojoinpage.input_phone(self.phone)
		uokojoinpage.set_password('123456')
		uokojoinpage.confirm_password('123456')
		uokojoinpage.drage_slider()
		sleep(8)                     #此处不要时间太短 验证码要一定时间才能收到
		uokojoinpage.input_smscode(publicfunction.get_smscode())
		uokojoinpage.submit_join_button()
		sleep(3)
		self.assertIn('注册成功', uokojoinpage.join_page_source(),msg='注册不成功')









				
		
		
		
		
		
		