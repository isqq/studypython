#安控4.5部署测试
import time,os,re
from case.check import Check
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


#4.5用例
class Ak45(Check):
	# def case1(self):
	# 	#编写__doc__,执行用例失败时,会输出用例名称,请自定义用例内容
	# 	# 导入用户license
	# 	self.xclick('//*[@id="Main"]/div[3]/div[1]/ul/li[8]/ul/li[4]/span[2]')
	# 	self.xsendkey('//*[@id="Main"]/div[3]/div[2]/div[1]/div[2]/div[1]/div[3]/div/input',os.path.abspath("file/auto.lic"))
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div[2]/div/div/div[3]/button[1]')
	# 	self.userquit()
	# def case2(self):
	# 	'''切换超级管理员登录'''
	# 	self.login(username='superadmin@poctest1',password='11111111')
	# 	time.sleep(1)
	# 	self.xsendkey('//*[@id="Main"]/div[9]/div/div[2]/div/form/div[1]/div/div/input','11111111')
	# 	self.xsendkey('//*[@id="Main"]/div[9]/div/div[2]/div/form/div[2]/div/div/input','1qaz@WSX')
	# 	self.xsendkey('//*[@id="Main"]/div[9]/div/div[2]/div/form/div[3]/div/div/input','1qaz@WSX')
	# 	self.xclick('//*[@id="Main"]/div[9]/div/div[3]/div/button[1]/span')
	# def case3(self):
	# 	'''创建部门'''
	# 	self.xclick('//*[@id="Main"]/div[3]/div[1]/ul/li[7]/div')
	# 	self.xclick('//*[@id="Main"]/div[3]/div[1]/ul/li[7]/ul/li[1]/span[2]')
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[1]/div[1]/button')
	# 	self.xsendkey('//*[@id="Main"]/div[3]/div[2]/div/div/div[4]/div/div/form/div[2]/div/div/input','维护测试')
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[4]/div/div/div[2]/button[1]')
	# def case4(self):
	# 	'''创建管理员角色'''
	# 	self.xclick('//*[@id="Main"]/div[3]/div[1]/ul/li[7]/ul/li[2]/span[2]')
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[1]/div[1]/button')
	# 	self.xsendkey('//*[@id="Main"]/div[3]/div[2]/div/div/div[4]/div/div/form/div[1]/div/div/input','维护管理员')
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[4]/div/div/form/div[2]/div/div/label[2]/span[2]')
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[4]/div/div/div[2]/button[1]')
	# def case5(self):
	# 	'''创建管理员'''
	# 	self.xclick('//*[@id="Main"]/div[3]/div[1]/ul/li[7]/ul/li[3]/span[2]')
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[1]/div[1]/button')
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[4]/div/div/form/div[1]/div/div/div/input')
	# 	self.xsendkey('//*[@id="Main"]/div[3]/div[2]/div/div/div[4]/div/div/form/div[1]/div/div/div/input',Keys.DOWN)
	# 	self.xsendkey('//*[@id="Main"]/div[3]/div[2]/div/div/div[4]/div/div/form/div[1]/div/div/div/input',Keys.ENTER)
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[4]/div/div/form/div[2]/div/div/div/input')
	# 	self.xsendkey('//*[@id="Main"]/div[3]/div[2]/div/div/div[4]/div/div/form/div[2]/div/div/div/input',Keys.DOWN)
	# 	self.xsendkey('//*[@id="Main"]/div[3]/div[2]/div/div/div[4]/div/div/form/div[2]/div/div/div/input',Keys.ENTER)
	# 	self.xsendkey('//*[@id="Main"]/div[3]/div[2]/div/div/div[4]/div/div/form/div[3]/div/div/input','manager1')
	# 	self.xsendkey('//*[@id="Main"]/div[3]/div[2]/div/div/div[4]/div/div/form/div[4]/div/div/input','1qaz!QAZ')
	# 	self.xsendkey('//*[@id="Main"]/div[3]/div[2]/div/div/div[4]/div/div/form/div[5]/div/div/input','1qaz!QAZ')
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[4]/div/div/div[2]/button[1]')
	# 	self.userquit()
	# def case6(self):
	# 	'''切换管理员登录'''
	# 	self.login(username='manager1',password='1qaz!QAZ')#1qaz!QAZ
	# 	self.xsendkey('//*[@id="Main"]/div[9]/div/div[2]/div/form/div[1]/div/div/input','1qaz!QAZ')
	# 	self.xsendkey('//*[@id="Main"]/div[9]/div/div[2]/div/form/div[2]/div/div/input','1qaz@WSX')
	# 	self.xsendkey('//*[@id="Main"]/div[9]/div/div[2]/div/form/div[3]/div/div/input','1qaz@WSX')
	# 	self.xclick('//*[@id="Main"]/div[9]/div/div[3]/div/button[1]/span')
	# def case7(self):
	# 	'''创建开发角色'''
	# 	self.xclick('//*[@id="Main"]/div[3]/div[1]/ul/li[7]/div')
	# 	self.xclick('//*[@id="Main"]/div[3]/div[1]/ul/li[7]/ul/li[1]/span[2]')
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[1]/div[1]/button')
	# 	self.xsendkey('//*[@id="Main"]/div[3]/div[2]/div/div/div[4]/div/div/form/div[1]/div/div/input','开发')
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[4]/div/div/form/div[2]/div/div/label[2]/span[1]/span')
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[4]/div/div/form/div[5]/div/div/div/div[1]/div[4]/div[2]/label[10]/span[2]')
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[4]/div/div/form/div[5]/div/div/div/div[1]/div[4]/div[2]/label[11]/span[2]')
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[4]/div/div/form/div[5]/div/div/div/div[1]/div[4]/div[2]/label[12]/span[2]')
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[4]/div/div/div[2]/button[1]')
	# def case8(self):
	# 	'''创建审计者角色'''
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[1]/div[1]/button')
	# 	self.xsendkey('//*[@id="Main"]/div[3]/div[2]/div/div/div[4]/div/div/form/div[1]/div/div/input','审计')
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[4]/div/div/form/div[2]/div/div/label[2]/span[1]/span')
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[4]/div/div/form/div[5]/div/div/div/div[1]/div[4]/div[2]/label[6]/span[2]')
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[4]/div/div/form/div[5]/div/div/div/div[1]/div[4]/div[2]/label[7]/span[2]')
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[4]/div/div/form/div[5]/div/div/div/div[1]/div[4]/div[2]/label[8]/span[2]')
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[4]/div/div/form/div[5]/div/div/div/div[1]/div[4]/div[2]/label[9]/span[2]')
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[4]/div/div/form/div[5]/div/div/div/div[1]/div[4]/div[2]/label[13]/span[2]')
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[4]/div/div/div[2]/button[1]')
	# def case9(self):
	# 	'''创建开发'''
	# 	self.xclick('//*[@id="Main"]/div[3]/div[1]/ul/li[7]/ul/li[2]/span[2]')
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[1]/div[1]/button')
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[4]/div/div/form/div[1]/div/div/div/input')
	# 	self.xsendkey('//*[@id="Main"]/div[3]/div[2]/div/div/div[4]/div/div/form/div[1]/div/div/div/input',Keys.DOWN)
	# 	self.xsendkey('//*[@id="Main"]/div[3]/div[2]/div/div/div[4]/div/div/form/div[1]/div/div/div/input',Keys.DOWN)
	# 	self.xsendkey('//*[@id="Main"]/div[3]/div[2]/div/div/div[4]/div/div/form/div[1]/div/div/div/input',Keys.ENTER)
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[4]/div/div/form/div[2]/div/div/div/input')
	# 	self.xsendkey('//*[@id="Main"]/div[3]/div[2]/div/div/div[4]/div/div/form/div[2]/div/div/div/input',Keys.DOWN)
	# 	self.xsendkey('//*[@id="Main"]/div[3]/div[2]/div/div/div[4]/div/div/form/div[2]/div/div/div/input',Keys.ENTER)
	# 	self.xsendkey('//*[@id="Main"]/div[3]/div[2]/div/div/div[4]/div/div/form/div[3]/div/div/input','kaifa')
	# 	self.xsendkey('//*[@id="Main"]/div[3]/div[2]/div/div/div[4]/div/div/form/div[4]/div/div/input','1qaz!QAZ')
	# 	self.xsendkey('//*[@id="Main"]/div[3]/div[2]/div/div/div[4]/div/div/form/div[5]/div/div/input','1qaz!QAZ')
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[4]/div/div/div[2]/button[1]')
	# 	time.sleep(2)
	# def case10(self):
	# 	'''创建审计'''
	# 	self.xclick('//*[@id="Main"]/div[3]/div[1]/ul/li[7]/ul/li[2]/span[2]')
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[1]/div[1]/button')
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[4]/div/div/form/div[1]/div/div/div/input')
	# 	self.xsendkey('//*[@id="Main"]/div[3]/div[2]/div/div/div[4]/div/div/form/div[1]/div/div/div/input',Keys.UP)
	# 	self.xsendkey('//*[@id="Main"]/div[3]/div[2]/div/div/div[4]/div/div/form/div[1]/div/div/div/input',Keys.ENTER)
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[4]/div/div/form/div[2]/div/div/div/input')
	# 	self.xsendkey('//*[@id="Main"]/div[3]/div[2]/div/div/div[4]/div/div/form/div[2]/div/div/div/input',Keys.DOWN)
	# 	self.xsendkey('//*[@id="Main"]/div[3]/div[2]/div/div/div[4]/div/div/form/div[2]/div/div/div/input',Keys.ENTER)
	# 	self.xsendkey('//*[@id="Main"]/div[3]/div[2]/div/div/div[4]/div/div/form/div[3]/div/div/input','shenji')
	# 	self.xsendkey('//*[@id="Main"]/div[3]/div[2]/div/div/div[4]/div/div/form/div[4]/div/div/input','1qaz!QAZ')
	# 	self.xsendkey('//*[@id="Main"]/div[3]/div[2]/div/div/div[4]/div/div/form/div[5]/div/div/input','1qaz!QAZ')
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[4]/div/div/div[2]/button[1]')
	# 	time.sleep(2)
	# def case11(self):
	# 	'''上传签名文件'''
	# 	self.xclick('//*[@id="Main"]/div[3]/div[1]/ul/li[5]/div')
	# 	self.xclick('//*[@id="Main"]/div[3]/div[1]/ul/li[5]/ul/li[4]/span[2]')
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[1]/div[1]/button')
	# 	self.xsendkey('//*[@id="Main"]/div[3]/div[2]/div/div/div[6]/div/div/div[2]/form/div[1]/div[2]/div/input',os.path.abspath("file/mssp_server.keystore"))
	# 	self.xsendkey('//*[@id="Main"]/div[3]/div[2]/div/div/div[6]/div/div/div[2]/form/div[2]/div/textarea','poc_keystore')
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[6]/div/div/div[3]/button[1]')
	# 	time.sleep(2)
	# def case12(self):
	# 	'''创建Andriod应用'''
	# 	self.xclick('//*[@id="Main"]/div[3]/div[1]/ul/li[2]')
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[1]/div[1]/button')
	# 	self.xsendkey('//*[@id="Main"]/div[3]/div[2]/div/div/div[3]/div/div/form/div[1]/div/div/input','Android')
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[3]/div/div/form/div[2]/div/div/div[1]/input')
	# 	self.xsendkey('//*[@id="Main"]/div[3]/div[2]/div/div/div[3]/div/div/form/div[2]/div/div/div[1]/input',Keys.DOWN)
	# 	self.xsendkey('//*[@id="Main"]/div[3]/div[2]/div/div/div[3]/div/div/form/div[2]/div/div/div[1]/input',Keys.ENTER)
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[3]/div/div/div[2]/button[1]')
	# 	time.sleep(2)
	# def case13(self):
	# 	'''创建应用安全标准'''
	# 	self.xclick('//*[@id="Main"]/div[3]/div[1]/ul/li[4]/div')
	# 	time.sleep(1.5)
	# 	self.xclick('//*[@id="Main"]/div[3]/div[1]/ul/li[4]/ul/li[1]/span[2]')
	# 	time.sleep(1.5)
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[1]/div[2]/div[1]/div[1]/button')
	# 	time.sleep(1.5)
	# 	randlist=re.findall("el-collapse-content-\\d{3,5}",str(self.driver.page_source))
	# 	self.xsendkey("//*[@id='{}']/div/div/div[1]/div[1]/div[2]/div/div/input".format(randlist[0]),'维护应用标准')
	# 	time.sleep(1.5)
	# 	self.xclick("//*[@id='{}']/div/div/div/div/div[2]/div/div/label[1]/span[1]/span".format(randlist[3]))
	# 	time.sleep(1.5)
	# 	self.xclick("//*[@id='Main']/div[3]/div[2]/div/div/div[2]/form/div/div[2]/div/div")
	# 	time.sleep(1.5)
	# 	self.xclick("//*[@id='Main']/div[3]/div[2]/div/div/div[2]/form/div/div[3]/div/div")
	# 	time.sleep(1.5)
	# 	self.xclick("//*[@id='{}']/div/div/div[1]/div/div/div/div[1]/div[1]/label/span/span".format(randlist[7]))
	# 	time.sleep(1.5)
	# 	self.xclick("//*[@id='{}']/div/div/div[2]/div/div/div/div[1]/div[1]/label/span/span".format(randlist[7]))
	# 	time.sleep(1.5)
	# 	self.xclick("//*[@id='{}']/div/div/div[3]/div/div/div/div[1]/div[1]/label/span/span".format(randlist[7]))
	# 	time.sleep(1.5)
	# 	self.xclick("//*[@id='Main']/div[3]/div[2]/div/div/div[2]/form/div/div[4]/div/div")
	# 	time.sleep(1.5)
	# 	self.xclick("//*[@id='pane-fourth-platform']/div[4]/div/div[1]/div[2]/div[8]/div[2]/div[6]/div[1]/label/span/span")
	# 	time.sleep(1.5)
	# 	self.xclick("//*[@id='pane-fourth-platform']/div[4]/div/div[1]/div[2]/div[8]/div[2]/div[3]/div[1]/label/span/span")
	# 	time.sleep(1.5)
	# 	self.xclick("//*[@id='Main']/div[3]/div[2]/div/div/div[2]/div[1]/button[1]")
	# 	time.sleep(2)
	# def case14(self):
	# 	'''检查加固策略'''
	# 	self.xclick('//*[@id="Main"]/div[3]/div[1]/ul/li[5]/div')
	# 	self.xclick('//*[@id="Main"]/div[3]/div[1]/ul/li[5]/ul/li[1]')
	# 	if '已启用' in self.driver.page_source:
	# 		print('加固策略已存在,可继续测试')
	# 	else:
	# 		self.driver.quit()
	# 		print('请开启可用加固策略后再进行自动化测试')
	# 	time.sleep(2)
	# def case15(self):
	# 	'''创建android项目并分配'''
	# 	self.xclick('//*[@id="Main"]/div[3]/div[1]/ul/li[1]')
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[1]/div[1]/button')
	# 	randlist=re.findall("el-collapse-content-\\d{3,5}",str(self.driver.page_source))
	# 	self.xclick('//*[@id="{}"]/div/table/tr[1]/td[2]/div/div[1]/input'.format(randlist[0]))
	# 	self.xsendkey('//*[@id="{}"]/div/table/tr[1]/td[2]/div/div[1]/input'.format(randlist[0]),Keys.DOWN)
	# 	self.xsendkey('//*[@id="{}"]/div/table/tr[1]/td[2]/div/div[1]/input'.format(randlist[0]),Keys.ENTER)
	# 	self.xsendkey('//*[@id="{}"]/div/table/tr[3]/td[2]/div/input'.format(randlist[0]),'Android-auto')
	# 	self.xsendkey('//*[@id="{}"]/div/table/tr[4]/td[2]/div/input'.format(randlist[0]),'2.3')
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div/button[1]')
	# 	time.sleep(4)
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/table/tbody/tr/td[12]/div/a[1]')
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[4]/div/div/table/tr[3]/td/div/div[3]/div/div/div[2]/div/label[1]/span[1]/span')
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[4]/div/div/table/tr[3]/td/div/div[3]/div/div/div[2]/div/label[2]/span[1]/span')
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[4]/div/div/table/tr[3]/td/div/div[2]/div[1]/button')
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[4]/div/div/div[2]/button[1]')
	# 	self.userquit()
	# def case16(self):
	# 	'''切换开发登录并执行安全配置'''
	# 	self.login(username='kaifa',password='1qaz!QAZ')#1qaz!QAZ
	# 	self.xsendkey('//*[@id="Main"]/div[9]/div/div[2]/div/form/div[1]/div/div/input','1qaz!QAZ')
	# 	self.xsendkey('//*[@id="Main"]/div[9]/div/div[2]/div/form/div[2]/div/div/input','1qaz@WSX')
	# 	self.xsendkey('//*[@id="Main"]/div[9]/div/div[2]/div/form/div[3]/div/div/input','1qaz@WSX')
	# 	self.xclick('//*[@id="Main"]/div[9]/div/div[3]/div/button[1]/span')
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr/td[6]/div/a')
	# 	# 选择应用标准
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[2]/table/tr[4]/td[2]/button')
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[3]/div/div[2]/div/form/div[3]/div/div/div[1]/input')
	# 	self.xsendkey('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[3]/div/div[2]/div/form/div[3]/div/div/div[1]/input',Keys.DOWN)
	# 	self.xsendkey('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[3]/div/div[2]/div/form/div[3]/div/div/div[1]/input',Keys.ENTER)
	# 	time.sleep(2)
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[3]/div/div[3]/div/button[2]/span')
	# 	time.sleep(2)
	# 	# 选择加固流程
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[2]/table/tr[5]/td[2]/button')
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[4]/div/div[2]/div/form/div[1]/div/div/div[1]/input')
	# 	self.xsendkey('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[4]/div/div[2]/div/form/div[1]/div/div/div[1]/input',Keys.DOWN)
	# 	self.xsendkey('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[4]/div/div[2]/div/form/div[1]/div/div/div[1]/input',Keys.ENTER)
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[4]/div/div[3]/div/button[2]')
	# 	# 选择加固策略
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[2]/table/tr[6]/td[2]/button')
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[5]/div/div[2]/div/form/div[1]/div/div/div[1]/input')
	# 	self.xsendkey('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[5]/div/div[2]/div/form/div[1]/div/div/div[1]/input',Keys.DOWN)
	# 	self.xsendkey('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[5]/div/div[2]/div/form/div[1]/div/div/div[1]/input',Keys.ENTER)
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[5]/div/div[3]/div/button[1]')
	# 	time.sleep(1)
	# 	# 选择签名文件
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[2]/table/tr[7]/td[2]/button')
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[6]/div/div[2]/div/form/div[1]/div/div/div/input')
	# 	self.xsendkey('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[6]/div/div[2]/div/form/div[1]/div/div/div/input',Keys.DOWN)
	# 	self.xsendkey('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[6]/div/div[2]/div/form/div[1]/div/div/div/input',Keys.ENTER)
	# 	self.xsendkey('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[6]/div/div[2]/div/form/div[3]/div/div/input','mssp_server')
	# 	time.sleep(3)
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[6]/div/div[2]/div/form/div[4]/div/div/div[1]/input')
	# 	time.sleep(2)
	# 	self.xsendkey('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[6]/div/div[2]/div/form/div[4]/div/div/div[1]/input',Keys.DOWN)
	# 	self.xsendkey('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[6]/div/div[2]/div/form/div[4]/div/div/div[1]/input',Keys.DOWN)
	# 	self.xsendkey('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[6]/div/div[2]/div/form/div[4]/div/div/div[1]/input',Keys.ENTER)
	# 	self.xsendkey('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[6]/div/div[2]/div/form/div[5]/div/div/input','mssp_server')
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[6]/div/div[3]/div/button[1]')
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[1]/div/button')
	# 	#退出
	# 	self.userquit()
	# def case17(self):
	# 	'''切换审计者登录审计安全需求'''
	# 	self.login(username='shenji',password='1qaz!QAZ')#1qaz!QAZ
	# 	self.xsendkey('//*[@id="Main"]/div[9]/div/div[2]/div/form/div[1]/div/div/input','1qaz!QAZ')
	# 	self.xsendkey('//*[@id="Main"]/div[9]/div/div[2]/div/form/div[2]/div/div/input','1qaz@WSX')
	# 	self.xsendkey('//*[@id="Main"]/div[9]/div/div[2]/div/form/div[3]/div/div/input','1qaz@WSX')
	# 	self.xclick('//*[@id="Main"]/div[9]/div/div[3]/div/button[1]/span')
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr/td[6]/div/a')
	# 	self.xsendkey('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[2]/table[1]/tr/td[2]/div/textarea','同意此需求发布')
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[1]/div/button[1]')
	# 	#退出
	# 	self.userquit()
	# def case18(self):
	# 	'''切换开发执行至检测结果确认'''
	# 	self.login(username='kaifa',password='1qaz@WSX')
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[2]/td[6]/div/a')
	# 	self.driver.find_element_by_xpath('//*[@id="upload_form"]/div/div/div/div/div/input[2]').send_keys(os.path.abspath("file/auto.apk"))
	# 	time.sleep(2)
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[1]/div/button')
	# 	time.sleep(2)
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[3]/div/div/div[3]/button[1]')
	# 	time.sleep(7)
	# 	self.xclick('//*[@id="Main"]/div[3]/div[1]/ul/li[1]')
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[6]/div/a')
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[2]/table[1]/tr/td[2]/div/button[2]')
	# 	time.sleep(3)
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[3]/div/div/div[1]/button[1]')
	# 	time.sleep(2)
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[1]/div/button[1]')
	# 	#检查人工检测是否检测完成
	# 	self.status_check('检测报告')
	# 	#提交安全检测
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[1]/div/button[1]')
	# 	#提交应用加固
	# 	self.status_check('检测报告')
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[1]/div/button[1]')
	# 	#退出
	# 	self.userquit()
	# def case19(self):
	# 	'''切换审计者登录并执行至应用发布并下载应用'''
	# 	self.login(username='shenji',password='1qaz@WSX')
	# 	# 检测结果确认
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr/td[6]/div/a')
	# 	time.sleep(1)
	# 	self.xsendkey('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[2]/table[1]/tr/td[2]/div/textarea','结果已确认,同意发布')
	# 	time.sleep(1)
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[1]/div/button[1]')
	# 	time.sleep(1)
	# 	# 应用发布
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[1]/div/button')
	# 	time.sleep(1)
	# 	self.userquit()

	# def case21(self):
	# 	'''检查项目报告'''
	# 	self.login(username='manager1',password='1qaz@WSX')#1qaz!QAZ
	# 	time.sleep(2)
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/table/tbody/tr/td[12]/div/a[2]')
	# 	time.sleep(1)
	# 	if 'Android-auto-项目安全开发总结报告' in self.driver.page_source and '2.3' in self.driver.page_source:
	# 		pass
	# 	else:
	# 		print('项目报告数据错误')
	# 	self.xclick('//*[@id="Main"]/div[3]/div/div/div[1]/div/span[1]/span[1]')
	# 	time.sleep(2)
	# def case22(self):
	# 	'''检查应用报告'''
	# 	self.xclick('//*[@id="Main"]/div[3]/div[1]/ul/li[2]')
	# 	time.sleep(1)
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/table/tbody/tr/td[7]/div/a[2]')
	# 	time.sleep(1)
	# 	if 'Android-auto' in self.driver.page_source and '2.3' in self.driver.page_source:
	# 		pass
	# 	else:
	# 		print('应用报告数据错误')
	# 	self.xclick('//*[@id="Main"]/div[3]/div/div/div[1]/div/span[1]/span[1]')
	# 	time.sleep(1)
	# 	#self.userquit()
	# def case23(self):
	# 	'''创建IOS应用、项目并分配'''
	# 	# 创建iOS应用
	# 	self.xclick('//*[@id="Main"]/div[3]/div[1]/ul/li[2]')
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[1]/div[1]/button')
	# 	self.xsendkey('//*[@id="Main"]/div[3]/div[2]/div/div/div[3]/div/div/form/div[1]/div/div/input','Ios')
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[3]/div/div/form/div[2]/div/div/div[1]/input')
	# 	self.xsendkey('//*[@id="Main"]/div[3]/div[2]/div/div/div[3]/div/div/form/div[2]/div/div/div[1]/input',Keys.DOWN)
	# 	self.xsendkey('//*[@id="Main"]/div[3]/div[2]/div/div/div[3]/div/div/form/div[2]/div/div/div[1]/input',Keys.DOWN)
	# 	self.xsendkey('//*[@id="Main"]/div[3]/div[2]/div/div/div[3]/div/div/form/div[2]/div/div/div[1]/input',Keys.ENTER)
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[3]/div/div/div[2]/button[1]')
	# 	time.sleep(2)
	# 	# 创建ios应用安全标准
	# 	self.xclick('//*[@id="Main"]/div[3]/div[1]/ul/li[4]/div')
	# 	time.sleep(1.5)
	# 	self.xclick('//*[@id="Main"]/div[3]/div[1]/ul/li[4]/ul/li[1]/span[2]')
	# 	time.sleep(1.5)
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[1]/div[2]/div[1]/div[1]/button')
	# 	time.sleep(1.5)
	# 	randlist=re.findall("el-collapse-content-\\d{3,5}",str(self.driver.page_source))
	# 	self.xsendkey("//*[@id='{}']/div/div/div[1]/div[1]/div[2]/div/div/input".format(randlist[0]),'ios应用标准')
	# 	self.xclick('//*[@id="{}"]/div/div/div[1]/div[1]/div[3]/div/div/label[2]/span[2]'.format(randlist[1]))
	# 	time.sleep(1.5)
	# 	self.xclick("//*[@id='{}']/div/div/div/div/div[2]/div/div/label[1]/span[1]/span".format(randlist[3]))
	# 	time.sleep(1.5)
	# 	self.xclick("//*[@id='Main']/div[3]/div[2]/div/div/div[2]/form/div/div[2]/div/div")
	# 	time.sleep(1.5)
	# 	self.xclick("//*[@id='Main']/div[3]/div[2]/div/div/div[2]/form/div/div[3]/div/div")
	# 	time.sleep(1.5)
	# 	self.xclick("//*[@id='{}']/div/div/div[1]/div/div/div/div[1]/div[1]/label/span/span".format(randlist[7]))
	# 	time.sleep(1.5)
	# 	self.xclick("//*[@id='{}']/div/div/div[2]/div/div/div/div[1]/div[1]/label/span/span".format(randlist[7]))
	# 	time.sleep(1.5)
	# 	self.xclick("//*[@id='{}']/div/div/div[3]/div/div/div/div[1]/div[1]/label/span/span".format(randlist[7]))
	# 	time.sleep(2)
	# 	self.xclick("//*[@id='{}']/div/div/div[3]/div/div/div/div[1]/div[1]/label/span/span".format(randlist[7]))
	# 	time.sleep(1.5)
	# 	self.xclick("//*[@id='Main']/div[3]/div[2]/div/div/div[2]/form/div/div[4]/div/div")
	# 	time.sleep(1.5)
	# 	self.xclick("//*[@id='pane-fourth-platform']/div[4]/div/div[1]/div[2]/div[5]/div[2]/div[2]/div[1]/label/span/span")
	# 	time.sleep(1.5)
	# 	self.xclick("//*[@id='pane-fourth-platform']/div[4]/div/div[1]/div[2]/div[5]/div[2]/div[3]/div[1]/label/span/span")
	# 	time.sleep(1.5)
	# 	self.xclick("//*[@id='Main']/div[3]/div[2]/div/div/div[2]/div[1]/button[1]")
	# 	time.sleep(2)
	# 	# 创建iOS项目
	# 	self.xclick('//*[@id="Main"]/div[3]/div[1]/ul/li[1]')
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[1]/div[1]/button')
	# 	randlist=re.findall("el-collapse-content-\\d{3,5}",str(self.driver.page_source))
	# 	self.xclick('//*[@id="{}"]/div/table/tr[1]/td[2]/div/div[1]/input'.format(randlist[0]))
	# 	self.xsendkey('//*[@id="{}"]/div/table/tr[1]/td[2]/div/div[1]/input'.format(randlist[0]),Keys.DOWN)
	# 	self.xsendkey('//*[@id="{}"]/div/table/tr[1]/td[2]/div/div[1]/input'.format(randlist[0]),Keys.ENTER)
	# 	self.xsendkey('//*[@id="{}"]/div/table/tr[3]/td[2]/div/input'.format(randlist[0]),'Ios-auto')
	# 	self.xsendkey('//*[@id="{}"]/div/table/tr[4]/td[2]/div/input'.format(randlist[0]),'2.3')
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div/button[1]')
	# 	time.sleep(4)
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/table/tbody/tr/td[12]/div/a[1]')
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[4]/div/div/table/tr[3]/td/div/div[3]/div/div/div[2]/div/label[1]/span[1]/span')
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[4]/div/div/table/tr[3]/td/div/div[3]/div/div/div[2]/div/label[2]/span[1]/span')
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[4]/div/div/table/tr[3]/td/div/div[2]/div[1]/button')
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[4]/div/div/div[2]/button[1]')
	# 	self.userquit()
	# def case24(self):
	# 	'''切换开发登录并执行安全配置'''
	# 	self.login(username='kaifa',password='1qaz@WSX')#1qaz!QAZ
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr/td[6]/div/a')
	# 	# 选择应用标准
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[2]/table/tr[4]/td[2]/button')
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[3]/div/div[2]/div/form/div[3]/div/div/div/input')
	# 	self.xsendkey('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[3]/div/div[2]/div/form/div[3]/div/div/div[1]/input',Keys.DOWN)
	# 	self.xsendkey('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[3]/div/div[2]/div/form/div[3]/div/div/div[1]/input',Keys.ENTER)
	# 	time.sleep(3)
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[3]/div/div[3]/div/button[2]/span')
	# 	time.sleep(2)
	# 	# 选择流程
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[2]/table/tr[5]/td[2]/button')
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[4]/div/div[2]/div/form/div[1]/div/div/div/input')
	# 	self.xsendkey('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[4]/div/div[2]/div/form/div[1]/div/div/div[1]/input',Keys.DOWN)
	# 	self.xsendkey('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[4]/div/div[2]/div/form/div[1]/div/div/div[1]/input',Keys.ENTER)
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[4]/div/div[3]/div/button[2]')
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[1]/div/button')
	# 	time.sleep(2)
	# 	#退出
	# 	self.userquit()
	# def case25(self):
	# 	'''执行至检测结果确认'''
	# 	#切换到审计者进行安全需求确认
	# 	self.login(username='shenji',password='1qaz@WSX')
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr/td[6]/div/a')
	# 	self.xsendkey('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[2]/table[1]/tr/td[2]/div/textarea','同意此需求发布')
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[1]/div/button[1]')
	# 	#审计者退出
	# 	self.userquit()
	# 	#切换到开发执行至检测结果确认
	# 	self.login(username='kaifa',password='1qaz@WSX')
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[2]/td[6]/div/a')
	# 	time.sleep(2)
	# 	self.driver.find_element_by_xpath('//*[@id="upload_form"]/div[1]/div/div/div/div/input[2]').send_keys(os.path.abspath("file/auto1.ipa"))
	# 	time.sleep(2)
	# 	self.driver.find_element_by_xpath('//*[@id="upload_form"]/div[2]/div/div/div/div/input[2]').send_keys(os.path.abspath("file/auto2.ipa"))
	# 	time.sleep(5)
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[1]/div/button')
	# 	time.sleep(2)
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[3]/div/div/div[3]/button[1]')
	# 	time.sleep(5)
	# 	self.xclick('//*[@id="Main"]/div[3]/div[1]/ul/li[1]')
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[6]/div/a')
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[2]/table[1]/tr/td[2]/div/button[2]')
	# 	time.sleep(3)
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[3]/div/div/div[1]/button[1]')
	# 	time.sleep(2)
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[1]/div/button[1]')
	# 	#检查人工检测是否检测完成
	# 	self.status_check('检测报告')
	# 	#提交安全检测
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[1]/div/button[1]')
	# 	#退出
	# 	self.userquit()

	# def case26(self):
	# 	'''切换审计者登录并执行至应用发布并下载应用'''
	# 	self.login(username='shenji',password='1qaz@WSX')
	# 	# 检测结果确认
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr/td[6]/div/a')
	# 	time.sleep(1)
	# 	self.xsendkey('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[2]/table[1]/tr/td[2]/div/textarea','结果已确认,同意发布')
	# 	time.sleep(1)
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[1]/div/button[1]')
	# 	time.sleep(1)
	# 	# 应用发布
	# 	self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[1]/div/button')
	# 	time.sleep(1)
	# 	self.userquit()
	def case27(self):
		'''检查项目报告'''
		self.userquit()
		self.login(username='manager1',password='1qaz@WSX')#1qaz!QAZ
		time.sleep(2)
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[12]/div/a[2]')
		time.sleep(1)
		if 'Ios-auto-项目安全开发总结报告' in self.driver.page_source and '2.3' in self.driver.page_source:
			pass
		else:
			print('项目报告数据错误')
		self.xclick('//*[@id="Main"]/div[3]/div/div/div[1]/div/span[1]/span[1]')
		time.sleep(2)
		'''检查应用报告'''
		self.xclick('//*[@id="Main"]/div[3]/div[1]/ul/li[2]')
		time.sleep(1)
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[7]/div/a[2]')
		time.sleep(1)
		if 'Ios-auto' in self.driver.page_source and '2.3' in self.driver.page_source:
			pass
		else:
			print('应用报告数据错误')
		self.xclick('//*[@id="Main"]/div[3]/div/div/div[1]/div/span[1]/span[1]')
		time.sleep(1)
	def case28(self):
		'''切换项目管理员登录&创建WEB应用、项目并分配'''
		# 创建WEB应用
		self.xclick('//*[@id="Main"]/div[3]/div[1]/ul/li[2]')
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[1]/div[1]/button')
		self.xsendkey('//*[@id="Main"]/div[3]/div[2]/div/div/div[3]/div/div/form/div[1]/div/div/input','Web')
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[3]/div/div/form/div[2]/div/div/div[1]/input')
		self.xsendkey('//*[@id="Main"]/div[3]/div[2]/div/div/div[3]/div/div/form/div[2]/div/div/div[1]/input',Keys.DOWN)
		self.xsendkey('//*[@id="Main"]/div[3]/div[2]/div/div/div[3]/div/div/form/div[2]/div/div/div[1]/input',Keys.DOWN)
		self.xsendkey('//*[@id="Main"]/div[3]/div[2]/div/div/div[3]/div/div/form/div[2]/div/div/div[1]/input',Keys.DOWN)
		self.xsendkey('//*[@id="Main"]/div[3]/div[2]/div/div/div[3]/div/div/form/div[2]/div/div/div[1]/input',Keys.ENTER)
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[3]/div/div/div[2]/button[1]')
		time.sleep(2)
		# 创建WEB应用安全标准
		self.xclick('//*[@id="Main"]/div[3]/div[1]/ul/li[4]/div')
		time.sleep(1.5)
		self.xclick('//*[@id="Main"]/div[3]/div[1]/ul/li[4]/ul/li[1]/span[2]')
		time.sleep(1.5)
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[1]/div[2]/div[1]/div[1]/button')
		time.sleep(1.5)
		randlist=re.findall("el-collapse-content-\\d{3,5}",str(self.driver.page_source))
		self.xsendkey("//*[@id='{}']/div/div/div[1]/div[1]/div[2]/div/div/input".format(randlist[0]),'Web应用标准')
		self.xclick('//*[@id="{}"]/div/div/div[1]/div[1]/div[3]/div/div/label[3]/span[2]'.format(randlist[1]))
		time.sleep(1.5)
		self.xclick("//*[@id='{}']/div/div/div/div/div[2]/div/div/label[1]/span[1]/span".format(randlist[3]))
		time.sleep(1.5)
		self.xclick("//*[@id='Main']/div[3]/div[2]/div/div/div[2]/form/div/div[2]/div/div")
		time.sleep(1.5)
		self.xclick("//*[@id='Main']/div[3]/div[2]/div/div/div[2]/form/div/div[3]/div/div")
		time.sleep(1.5)
		self.xclick("//*[@id='{}']/div/div/div[1]/div/div/div/div[1]/div[1]/label/span/span".format(randlist[7]))
		time.sleep(1.5)
		self.xclick("//*[@id='{}']/div/div/div[2]/div/div/div/div[1]/div[1]/label/span/span".format(randlist[7]))
		time.sleep(1.5)
		self.xclick("//*[@id='{}']/div/div/div[3]/div/div/div/div[1]/div[1]/label/span/span".format(randlist[7]))
		time.sleep(2)
		self.xclick("//*[@id='{}']/div/div/div[3]/div/div/div/div[1]/div[1]/label/span/span".format(randlist[7]))
		time.sleep(1.5)
		self.xclick("//*[@id='Main']/div[3]/div[2]/div/div/div[2]/form/div/div[4]/div/div")
		time.sleep(1.5)
		self.xclick("//*[@id='pane-fourth-platform']/div[4]/div/div[1]/div[2]/div[7]/div[2]/div[1]/div[1]/label/span/span")
		time.sleep(1.5)
		self.xclick("//*[@id='pane-fourth-platform']/div[4]/div/div[1]/div[2]/div[7]/div[2]/div[2]/div[1]/label/span/span")
		time.sleep(1.5)
		self.xclick("//*[@id='Main']/div[3]/div[2]/div/div/div[2]/div[1]/button[1]")
		time.sleep(2)
		# 创建WEB项目并分配
		self.xclick('//*[@id="Main"]/div[3]/div[1]/ul/li[1]')
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[1]/div[1]/button')
		randlist=re.findall("el-collapse-content-\\d{3,5}",str(self.driver.page_source))
		self.xclick('//*[@id="{}"]/div/table/tr[1]/td[2]/div/div[1]/input'.format(randlist[0]))
		self.xsendkey('//*[@id="{}"]/div/table/tr[1]/td[2]/div/div[1]/input'.format(randlist[0]),Keys.DOWN)
		self.xsendkey('//*[@id="{}"]/div/table/tr[1]/td[2]/div/div[1]/input'.format(randlist[0]),Keys.ENTER)
		self.xsendkey('//*[@id="{}"]/div/table/tr[3]/td[2]/div/input'.format(randlist[0]),'Web-auto')
		self.xsendkey('//*[@id="{}"]/div/table/tr[4]/td[2]/div/input'.format(randlist[0]),'1.3')
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div/button[1]')
		time.sleep(4)
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[12]/div/a[1]')
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[4]/div/div/table/tr[3]/td/div/div[3]/div/div/div[2]/div/label[1]/span[1]/span')
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[4]/div/div/table/tr[3]/td/div/div[3]/div/div/div[2]/div/label[2]/span[1]/span')
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[4]/div/div/table/tr[3]/td/div/div[2]/div[1]/button')
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[4]/div/div/div[2]/button[1]')
		self.userquit()
	def case29(self):
		'''切换登录并执行安全配置'''
		#切换至开发配置安全需求
		self.login(username='kaifa',password='1qaz@WSX')#1qaz!QAZ
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[6]/div/a')
		# 选择应用标准
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[2]/table/tr[4]/td[2]/button')
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[3]/div/div[2]/div/form/div[3]/div/div/div/input')
		self.xsendkey('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[3]/div/div[2]/div/form/div[3]/div/div/div[1]/input',Keys.DOWN)
		self.xsendkey('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[3]/div/div[2]/div/form/div[3]/div/div/div[1]/input',Keys.ENTER)
		time.sleep(3)
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[3]/div/div[3]/div/button[2]/span')
		time.sleep(2)
		# 选择流程
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[2]/table/tr[5]/td[2]/button')
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[4]/div/div[2]/div/form/div[1]/div/div/div/input')
		self.xsendkey('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[4]/div/div[2]/div/form/div[1]/div/div/div[1]/input',Keys.DOWN)
		self.xsendkey('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[4]/div/div[2]/div/form/div[1]/div/div/div[1]/input',Keys.ENTER)
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[4]/div/div[3]/div/button[2]')
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[1]/div/button')
		time.sleep(2)
		#退出
		self.userquit()
		#切换至审计进行安全需求确认
		self.login(username='shenji',password='1qaz@WSX')
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr/td[6]/div/a')
		self.xsendkey('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[2]/table[1]/tr/td[2]/div/textarea','同意此需求发布')
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[1]/div/button[1]')
		#审计者退出
		self.userquit()
	def case30(self):
		'''切换至开发执行至检测结果确认'''
		self.login(username='kaifa',password='1qaz@WSX')
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[2]/td[6]/div/a')
		time.sleep(2)
		self.xsendkey('//*[@id="upload_form"]/div/div/div/div/input','http://www.baidu.com')
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[1]/div/button')
		time.sleep(2)
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[3]/div/div/div[3]/button[1]')
		time.sleep(5)
		self.xclick('//*[@id="Main"]/div[3]/div[1]/ul/li[1]')
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[6]/div/a')
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[2]/table[1]/tr/td[2]/div/button[2]')
		time.sleep(3)
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[3]/div/div/div[1]/button[1]')
		time.sleep(2)
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[1]/div/button[1]')
		#检查人工检测是否检测完成
		self.web_check('检测报告')
		#提交安全检测
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[1]/div/button[1]')
		#退出
		self.userquit()
	def case31(self):
		'''切换审计登录并执行检测结果确认'''
		self.login(username='shenji',password='1qaz@WSX')
		# 检测结果确认
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr/td[6]/div/a')
		time.sleep(1)
		self.xsendkey('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[2]/table[1]/tr/td[2]/div/textarea','结果已确认,同意发布')
		time.sleep(1)
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[1]/div/button[1]')
		time.sleep(1)
		# 应用发布
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[3]/div[1]/div/button')
		time.sleep(1)
		self.userquit()
	def case32(self):
		'''检查项目报告'''
		self.login(username='manager1',password='1qaz@WSX')#1qaz!QAZ
		time.sleep(2)
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[12]/div/a[2]')
		time.sleep(1)
		if 'Web-auto-项目安全开发总结报告' in self.driver.page_source and '1.3' in self.driver.page_source:
			pass
		else:
			print('项目报告数据错误')
		self.xclick('//*[@id="Main"]/div[3]/div/div/div[1]/div/span[1]/span[1]')
		time.sleep(2)
		'''检查应用报告'''
		self.xclick('//*[@id="Main"]/div[3]/div[1]/ul/li[2]')
		time.sleep(1)
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[7]/div/a[2]')
		time.sleep(1)
		if 'Web-auto' in self.driver.page_source and '1.3' in self.driver.page_source:
			pass
		else:
			print('应用报告数据错误')
		self.xclick('//*[@id="Main"]/div[3]/div/div/div[1]/div/span[1]/span[1]')
		time.sleep(1)
		self.userquit()
	def case33(self):
		'''切换超级管理员并检查综合安全报告'''
		self.login(username='superadmin@poctest1',password='1qaz@WSX')
		time.sleep(1)
		self.xclick('//*[@id="Main"]/div[3]/div[1]/ul/li[8]')
		time.sleep(1)
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div[1]/a/button')
		time.sleep(1)
		if 'Android-auto' in self.driver.page_source and '3.3' in self.driver.page_source:
			pass
		else:
			print('综合开发报告数据错误')
		time.sleep(1)
		self.xclick('//*[@id="Main"]/div[3]/div[1]/div/label[1]/span')
		time.sleep(1)
		self.xclick('//*[@id="Main"]/div[3]/div[1]/ul/li[1]/span')
		time.sleep(1)
		self.xclick('//*[@id="Main"]/div[3]/div[1]/ul/li[1]')
		time.sleep(2)
	def case34(self):
		'''检查源码用户是否同步'''
		time.sleep(1)
		self.xclick('//*[@id="Main"]/div[3]/div[1]/ul/li[6]/div')
		self.xclick('//*[@id="Main"]/div[3]/div[1]/ul/li[6]/ul/li[3]/span[2]')
		time.sleep(1)
		if '没有同步' in self.driver.page_source:
			print('源码同步账号失败')
	def case35(self):
		'''提交应用加固'''
		time.sleep(1)
		self.xclick('//*[@id="Main"]/div[3]/div[1]/ul/li[6]/ul/li[2]')
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[1]/div/button')
		time.sleep(2)
		self.xsendkey('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[5]/div/div/div[2]/form/div[1]/div[2]/div/input',os.path.abspath("file/auto.apk"))
		time.sleep(4)
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[5]/div/div/div[2]/form/div[5]/div/div[1]/input')
		self.xsendkey('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[5]/div/div/div[2]/form/div[5]/div/div[1]/input',Keys.DOWN)
		self.xsendkey('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[5]/div/div/div[2]/form/div[5]/div/div[1]/input',Keys.ENTER)
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[5]/div/div/div[3]/button[1]')
		self.status_check('加固成功')
		time.sleep(2)
	def case36(self):
		'''提交SDK加固'''
		time.sleep(1)
		self.xclick('//*[@id="Main"]/div[3]/div[1]/ul/li[6]/ul/li[4]')
		time.sleep(2)
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[1]/div/button')
		time.sleep(2)
		self.xsendkey('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[5]/div/div/div[2]/form/div[1]/div[2]/div/input',os.path.abspath("file/auto.zip"))
		time.sleep(4)
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[5]/div/div/div[2]/form/div[5]/div/div/input')
		self.xsendkey('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[5]/div/div/div[2]/form/div[5]/div/div/input',Keys.DOWN)
		self.xsendkey('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[5]/div/div/div[2]/form/div[5]/div/div/input',Keys.ENTER)
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[5]/div/div/div[3]/button[1]')
		self.status_check('加固成功')
		time.sleep(2)
	def case37(self):
		'''提交HTML5加固'''
		self.xclick('//*[@id="Main"]/div[3]/div[1]/ul/li[6]/ul/li[5]')
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[1]/div/button')
		time.sleep(2)
		self.xsendkey('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[5]/div/div/div[2]/form/div[1]/div[2]/div/input',os.path.abspath("file/auto.zip"))
		time.sleep(4)
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[5]/div/div/div[2]/form/div[5]/div/div/input')
		self.xsendkey('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[5]/div/div/div[2]/form/div[5]/div/div/input',Keys.DOWN)
		self.xsendkey('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[5]/div/div/div[2]/form/div[5]/div/div/input',Keys.ENTER)
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[5]/div/div/div[3]/button[1]')
		self.status_check('加固成功')
		time.sleep(2)
	def case38(self):
		'''创建安全密钥白盒库及安全密钥'''
		time.sleep(1)
		self.xclick('//*[@id="Main"]/div[3]/div[1]/ul/li[6]/ul/li[6]')
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div/div[2]/div/button[1]')
		time.sleep(2)
		self.xsendkey('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/form/div[1]/div/div[1]/input','test')
		time.sleep(4)
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/form/div[2]/div/div/label[1]/span[2]')
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/form/div[3]/div/div/label[1]/span[2]')
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/form/div[4]/div/div/label[2]/span[2]')
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/form/div[6]/div/label/span[2]')
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/form/div[7]/div/button[1]')
		self.status_check('生成成功')
		time.sleep(2)
	def case39(self):
		'''创建安全组件库'''
		self.xclick('//*[@id="Main"]/div[3]/div[1]/ul/li[6]/ul/li[7]')
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div/button')
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div/div[1]/button')
		time.sleep(2)
		self.xsendkey('//*[@id="add_dev_com"]/div[1]/div/input','test')
		self.xsendkey('//*[@id="add_dev_com"]/div[2]/div/div[1]/input','test')
		self.xsendkey('//*[@id="add_dev_com"]/div[3]/div/div[1]/input','test')
		self.xsendkey('//*[@id="add_dev_com"]/div[5]/div/div/div[1]/div/input','test')
		self.xsendkey('//*[@id="add_dev_com"]/div[5]/div/div/div[2]/div/textarea','test')
		self.xclick('//*[@id="add_dev_com"]/div[6]/div/div/div[3]/label/span[1]')
		self.xsendkey('//*[@id="add_dev_com"]/div[6]/div/div/div[1]/div/input','test')
		self.xsendkey('//*[@id="add_dev_com"]/div[6]/div/div/div[3]/div/input','http://www.test.com')
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div/div[3]/button[1]')

	def case40(self):
		'''删除应用、项目'''
		# 删除项目
		self.xclick('//*[@id="Main"]/div[3]/div[1]/ul/li[1]')
		time.sleep(1)
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/table/thead/tr/th[1]/div/label/span/span')
		time.sleep(1)
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[2]/div[3]/div/button')
		time.sleep(1)
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[5]/div/div/div[3]/button[1]')
		time.sleep(2)
		# 删除应用
		self.xclick('//*[@id="Main"]/div[3]/div[1]/ul/li[2]')
		time.sleep(1)
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/table/thead/tr/th[1]/div/label/span')
		time.sleep(1)
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[2]/div[3]/div/button')
		time.sleep(1)
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[6]/div/div/div[3]/button[1]')
		time.sleep(2)
	def case41(self):
		'''删除通用、自定义标准'''
		self.xclick('//*[@id="Main"]/div[3]/div[1]/ul/li[4]/div')
		time.sleep(1)
		self.xclick('//*[@id="Main"]/div[3]/div[1]/ul/li[4]/ul/li[1]')
		time.sleep(1)
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/table/thead/tr/th[1]/div/label/span')
		time.sleep(1)
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[1]/div[2]/div[2]/div[3]/div/button')
		time.sleep(1)
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[3]/div/div/div[3]/button[1]')
		time.sleep(2)
	def case42(self):
		'''删除加固数据、安全组件、密钥白盒'''
		#删除应用加固
		self.xclick('//*[@id="Main"]/div[3]/div[1]/ul/li[6]/div')
		self.xclick('//*[@id="Main"]/div[3]/div[1]/ul/li[6]/ul/li[2]')
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[2]/div[1]/div[2]/table/thead/tr/th[1]/div/label/span')
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/div/button')
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[4]/div/div/div[3]/button[1]')
		time.sleep(2)
		#删除SDK加固
		self.xclick('//*[@id="Main"]/div[3]/div[1]/ul/li[6]/ul/li[4]')
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[2]/div[1]/div[2]/table/thead/tr/th[1]/div/label/span')
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/div/button')
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[4]/div/div/div[3]/button[1]')
		time.sleep(2)
		#删除HTML5加固
		self.xclick('//*[@id="Main"]/div[3]/div[1]/ul/li[6]/ul/li[5]')
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[2]/div[1]/div[2]/table/thead/tr/th[1]/div/label/span')
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/div/button')
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[4]/div/div/div[3]/button[1]')
		time.sleep(2)
		#删除安全密钥白盒
		self.xclick('//*[@id="Main"]/div[3]/div[1]/ul/li[6]/ul/li[6]')
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div/div[3]/div[2]/div[3]/table/tbody/tr/td[9]/div/a[2]')
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div/div[4]/div/div/div[3]/button[1]')
		time.sleep(2)
		#删除安全组件
		self.xclick('//*[@id="Main"]/div[3]/div[1]/ul/li[6]/ul/li[7]')
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div/button')
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div/div[2]/div[1]/div[3]/table/tbody/tr/td[5]/div/a[2]')
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[3]/div/div/div[3]/button[1]')
		time.sleep(2)
	def case43(self):
		'''删除角色、用户'''
		# 删用户
		self.xclick('//*[@id="Main"]/div[3]/div[1]/ul/li[7]/div')
		time.sleep(1)
		self.xclick('//*[@id="Main"]/div[3]/div[1]/ul/li[7]/ul/li[3]/span[2]')
		time.sleep(1)
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/table/thead/tr/th[1]/div/label/span')
		time.sleep(1)
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[2]/div[3]/div/button')
		time.sleep(1)
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[3]/div/div/div[3]/button[1]')
		time.sleep(1)
		# 删角色
		self.xclick('//*[@id="Main"]/div[3]/div[1]/ul/li[7]/ul/li[2]')
		time.sleep(1)
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/table/thead/tr/th[1]/div/label/span')
		time.sleep(1)
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[2]/div[3]/div/button')
		time.sleep(1)
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[3]/div/div/div[3]/button[1]')
		time.sleep(1)
		# 删部门
		self.xclick('//*[@id="Main"]/div[3]/div[1]/ul/li[7]/ul/li[1]/span[2]')
		time.sleep(1)
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/table/tbody/tr/td[1]/div/label/span')
		time.sleep(1)
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[2]/div[3]/div/button')
		time.sleep(1)
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[3]/div/div/div[3]/button[1]')
		time.sleep(1)
		# 退出
		self.userquit()
	def case44(self):
		'''切换系统管理员登录,删除客户'''
		self.login(username='sysadmin',password='AK3JRq#VNGH7@mbw')
		time.sleep(1)
		self.xclick('//*[@id="Main"]/div[3]/div[1]/ul/li[6]/div')
		time.sleep(1)
		self.xclick('//*[@id="Main"]/div[3]/div[1]/ul/li[6]/ul/li[1]/span[2]')
		time.sleep(1)
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/table/tbody/tr/td[1]/div/label/span')
		time.sleep(1)
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[2]/div[2]/div[3]/div/button')
		time.sleep(1)
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div/div/div[3]/div/div/div[3]/button[1]')
		time.sleep(1)
		self.userquit()
		time.sleep(1)
		self.driver.quit()
