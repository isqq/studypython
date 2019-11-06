#setting.py
import time
from selenium import webdriver
from tool.tools import Getcode

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class Setting:
	def __init__(self):
		self.inputurl()
		self.option=webdriver.ChromeOptions()
		self.option.add_argument("disable-infobars")
		self.driver=webdriver.Chrome(chrome_options=self.option)
		self.driver.maximize_window()#最大化窗口
		self.driver.get(self.url)#跳转到输入的地址相对应的页面
		self.login()
	def inputurl(self):
		#输入测试地址
		print('################################################')
		print('请输入你要测试的IP地址(http://或者https://)')
		while 1:
			self.url=str(input('>>>>'))
			if 'http://' in self.url or 'https://' in self.url:
				break
			else:
				print('地址输入错误,请重新输入')
	def login(self,username='sysadmin',password='AK3JRq#VNGH7@mbw'):
		#登录,具体元素请自定位
		time.sleep(2)
		self.driver.find_element_by_xpath('//*[@id="username"]').send_keys(username)
		self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)
		code=Getcode(self.driver.page_source,self.driver.get_cookies(),self.url).codeToString()
		self.driver.find_element_by_xpath('//*[@id="auth-code"]').send_keys(code)
		self.driver.find_element_by_xpath('//*[@id="bangcle"]/div/div[3]/div/form/button').click()
		time.sleep(5)
		self.login_check()
	def login_check(self):
		#登录检查,判断页面源码是否改变,是否登录成功
		if '登 录' in self.driver.page_source:
			print(r'验证码识别失败,重新识别中(识别率85%)')
			self.login_again()
		else:
			pass
	def login_again(self):
		#再次登录
		code=Getcode(self.driver.page_source,self.driver.get_cookies(),self.url).codeToString()
		self.driver.find_element_by_xpath('//*[@id="auth-code"]').send_keys(code)
		time.sleep(1)
		self.driver.find_element_by_xpath('//*[@id="bangcle"]/div/div[3]/div/form/button').click()
		time.sleep(2)
		self.login_check()
	def userquit(self):
		#用户退出,具体元素请自定位
		time.sleep(2)
		quit=self.driver.find_element_by_xpath('//*[@id="lg_header"]/div/div[2]/div[1]/span')
		ActionChains(self.driver).move_to_element(quit).perform()
		time.sleep(2)
		self.driver.find_element_by_xpath('//*[@id="lg_header"]/div/div[2]/div[1]/div/div/ul/li[3]').click()
	def system_check(self,value,name):
		#自定义系统联动状态检查功能
		if value=='已连接':
			pass
		else:
			print('{}未连接,请配置好联动配置,再进行自动化测试'.format(name))
			self.driver.quit()
	def status_check(self,value):
		#自定义流程中状态检查功能
		passkey=True
		while passkey:
			if value in self.driver.page_source:
				passkey=False
			else:
				time.sleep(20)
				self.driver.refresh()
	def web_check(self,value):
		# web流程中状态检查功能
		flag = True
		while flag :
			if value in self.driver.page_source :
				flag = False
			else:
				time.sleep(360)
				self.driver.refresh()
	def content_check(self,value):
		#文案检查
		if value in self.driver.page_source:
			pass
		else:
			self.driver.quit()
			print('{}异常'.format(value))
	def xclick(self,param):
		#xpath().click()的转换函数,每条后增加睡眠时间,避免代码冗余及因响应问题无法定位
		self.driver.find_element_by_xpath(param).click()
		time.sleep(1.2)
	def xsendkey(self,param,key):
		#xpath().sendkey()的转换函数,同xclick
		self.driver.find_element_by_xpath(param).send_keys(key)
		time.sleep(1.2)
	def getwindow(self):
		#查找当前窗口
		self.driver.switch_to_window(self.driver.window_handles[0])
