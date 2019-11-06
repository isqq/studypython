#初始化webdriver
import time
from bs4 import BeautifulSoup
from setting import Setting

#检查各项联动配置
class Check(Setting):
	def check1(self):
		'''加固联动配置'''
		time.sleep(1)
		self.xclick('//*[@id="Main"]/div[3]/div[1]/ul/li[8]/div')
		self.driver.find_element_by_xpath('//*[@id="Main"]/div[3]/div[1]/ul/li[8]/ul/li[3]/span[2]').click()
		time.sleep(1)
		html=BeautifulSoup(self.driver.page_source,'lxml')
		status=[i.text.strip() for i in html.select('#Main > div.main-contend.manage-platf > div.container > div > div > div > div.field.mt26 > table > tr:nth-child(6) > td:nth-child(2) > div')][0]
		self.system_check(status,'应用加固')
	def check2(self):
		'''测评联动配置'''
		time.sleep(1)
		self.driver.find_element_by_xpath('//*[@id="Main"]/div[3]/div[2]/div/ul/li[2]').click()
		time.sleep(1)
		html=BeautifulSoup(self.driver.page_source,'lxml')
		status=[i.text.strip() for i in html.select('#Main > div.main-contend.manage-platf > div.container > div > div > div > div.field.mt26 > table > tr:nth-child(6) > td:nth-child(2) > div')][0]
		time.sleep(1)
		self.system_check(status,'安全测评')
	def check3(self):
		'''密钥白盒联动配置'''
		time.sleep(1)
		self.driver.find_element_by_xpath('//*[@id="Main"]/div[3]/div[2]/div/ul/li[3]').click()
		time.sleep(1)
		html=BeautifulSoup(self.driver.page_source,'lxml')
		status=[i.text.strip() for i in html.select('div.set-status')][0]
		time.sleep(1)
		self.system_check(status,'密钥白盒')
	def check4(self):
	 	'''源码加固联动配置'''
	 	self.driver.find_element_by_xpath('//*[@id="Main"]/div[3]/div[2]/div/ul/li[4]').click()
	 	time.sleep(1)
	 	html=BeautifulSoup(self.driver.page_source,'lxml')
	 	status=[i.text.strip() for i in html.select('div.set-status')][0]
	 	self.system_check(status,'源码加固')
