#coding=utf-8
from config import globalparam
import pymssql
import random
import requests
import conn_db

	# 截图放到report下的img目录下
def get_img(dr, filename):
	path = globalparam.img_path + '\\' + filename
	dr.take_screenshot(path)

	# 随机产生手机号和身份证  参考 http://www.cnblogs.com/yicaifeitian/p/4668769.html
def createphone():
	prelist=["130","131","132","133","134","135","136","137","138","139","147","150","151","152","153",
	         "155","156","157","158","159","186","187","188"]
	phone = random.choice(prelist)+"".join(random.choice("0123456789") for i in range(8))
	return phone

	# 获取数据库验证码  参考 http://www.cnblogs.com/SunnyZhu/p/5603521.html

def get_smscode1():
	conn = pymssql.connect(host='115.159.93.131',
                       port= "8157",user='pre', password='c/3jtMDX9dWslGUo0KDm', database='Star-Main',charset="UTF-8")
	"""
   # 如果和本机数据库交互，只需修改链接字符串
    #conn=pymssql.connect(host='.',database='Michael')
	"""
	cur = conn.cursor()
	sql="select top 1 replace(SUBSTRING(content,CHARINDEX('：',content),7),'：','') from[Star-Notify].[dbo].[SMSTaskRecord] where Content like '%验证码%'  order by TaskCreateTime desc"
	cur.execute(sql)
	# 如果update/delete/insert记得要conn.commit()
	# 否则数据库事务无法提交
	query_smscode = cur.fetchone()
	cur.close()
	conn.close()
	return query_smscode[0]
# 这种直接调用数据库更方便
def get_smscode():
	sql="select top 1 replace(SUBSTRING(content,CHARINDEX('：',content),7),'：','') from[Star-Notify].[dbo].[SMSTaskRecord] where Content like '%验证码%'  order by TaskCreateTime desc"
	sms_code = str(conn_db.execute(sql))
	# sms_code = conn_db.execute(sql)
	code = filter(lambda x:x.isdigit(),sms_code) # 过滤掉数字外的字符
	return code
	#return sms_code[0]

print get_smscode1()
print get_smscode()
print createphone()

# 请求
r = requests.get('http://www.pre.uoko.com/')
print r.status_code