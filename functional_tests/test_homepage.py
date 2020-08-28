from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from unittest import TestCase
from django.test import TestCase
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#browser.get('http://localhost:8000')

#try:
#	main = WebDriverWait(webdriver.Chrome("../functional_tests/chromedriver.exe"), 10).until(
#		EC.presence_of_element_located((By.CLASS_NAME, "col-md-8"))
#	)
#except:
#	webdriver.Chrome("../functional_tests/chromedriver.exe").quit()


class tests_portfolio_links(StaticLiveServerTestCase):
	def setUp(self):
		self.browser = webdriver.Chrome("../functional_tests/chromedriver.exe")

	def test_clickon_Projects(self):
		link = self.browser.get(self.live_server_url)
		link = self.browser.find_element_by_link_text("Portfolio").click()
		link = self.browser.find_element_by_class_name("box-1").find_element_by_link_text("Read more").click()
		add_url = self.browser.get(self.live_server_url + '/projects')
		self.assertEquals(
		link,
		add_url
		)
		time.sleep(2)

	def test_clickon_Education(self):
		link = self.browser.get(self.live_server_url)
		link = self.browser.find_element_by_link_text("Portfolio").click()
		link = self.browser.find_element_by_class_name("box-2").find_element_by_link_text("Read more").click()
		add_url = self.browser.get(self.live_server_url + '/education')
		self.assertEquals(
		link,
		add_url
		)
		time.sleep(2)
	
	def test_clickon_Skiils(self):
		link = self.browser.get(self.live_server_url)
		link = self.browser.find_element_by_link_text("Portfolio").click()
		link = self.browser.find_element_by_class_name("box-3").find_element_by_link_text("Read more").click()
		add_url = self.browser.get(self.live_server_url + '/skills')
		self.assertEquals(
		link,
		add_url
		)
		time.sleep(2)

	#The reason why i am commenting out the method teardown is because making use of it i got some errors related to the connection reset,
	#specifically the ConnectionResetError:[WinError 10054] An existing connection was forcibly closed by the remote host.
	#without the method tear down,all the windows open for testing the browser functionality remain open until the end and then all of them are closed
	#the result of the test is OK in both cases.
	#def tearDown(self):
	#	self.browser.close()
		

class tests_functional(StaticLiveServerTestCase):
	def setUp(self):
		self.browser = webdriver.Chrome("../functional_tests/chromedriver.exe")

	def test_there_is_Contactme(self):
		self.browser.get(self.live_server_url + '/contactme')
		self.assertIn('fxc866@student.bham.ac.uk',self.browser.page_source)	
		time.sleep(2)

	def test_there_is_Portfolio(self):
		self.browser.get(self.live_server_url + '/resume')
		self.assertIn('fabrizio',self.browser.page_source)	
		time.sleep(2)

	def test_there_is_Projects(self):
		self.browser.get(self.live_server_url + '/projects')
		self.assertIn('projects',self.browser.page_source)
		time.sleep(2)

	def test_there_is_Education(self):
		self.browser.get(self.live_server_url + '/education')
		self.assertIn('education',self.browser.page_source)
		time.sleep(2)

	def test_there_is_Skills(self):
		self.browser.get(self.live_server_url + '/skills')
		self.assertIn('skills',self.browser.page_source)
		time.sleep(2)

	def test_there_is_Homepage(self):
		self.browser.get(self.live_server_url + '/homepage')
		self.assertIn('Welcome to my website',self.browser.page_source)	
		time.sleep(2)
	
	#The reason why i am commenting out the method teardown is because making use of it i got some errors related to the connection reset,
	#specifically the ConnectionResetError:[WinError 10054] An existing connection was forcibly closed by the remote host.
	#without the method tear down,all the windows open for testing the browser functionality remain open until the end and then all of them are closed
	#the result of the test is OK in both cases.
	#def tearDown(self):
	#	self.browser.close()



class tests_BlogHomePage(StaticLiveServerTestCase):

	def setUp(self):
		self.browser = webdriver.Chrome("../functional_tests/chromedriver.exe")

	def tearDown(self):
		self.browser.close()

	def test_blog_list(self):
		self.browser.get(self.live_server_url + '/')	
		#user request the page
		text = self.browser.find_element_by_class_name('col-md-4')
		self.assertEquals(
			text.find_element_by_tag_name('h4').text,
			'My Django Blog'
			)		

		
	def test_navbar_clickon_Mydjangoblog(self):
		self.browser.get(self.live_server_url)
		url = self.live_server_url + '/'
		self.browser.find_element_by_tag_name('a').click()
		self.assertEquals(
			self.browser.current_url,
			url)

	def test_navbar_clickon_Home(self):
		self.browser.get(self.live_server_url)
		url = self.live_server_url + reverse('homepage')
		self.browser.find_element_by_partial_link_text("Home").click()
		self.assertEquals(self.browser.current_url, url)
		
	def test_navbar_clikon_Portfolio(self):
		self.browser.get(self.live_server_url)
		url = self.live_server_url + reverse('resume')
		self.browser.find_element_by_link_text("Portfolio").click()
		self.assertEquals(self.browser.current_url, url)

	def test_navbar_clickon_Contact(self):
		self.browser.get(self.live_server_url)
		url = self.live_server_url + reverse('contactme')
		self.browser.find_element_by_link_text("Contact").click()
		self.assertEquals(self.browser.current_url, url)

	#The reason why i am commenting out the method teardown is because making use of it i got some errors related to the connection reset,
	#specifically the ConnectionResetError:[WinError 10054] An existing connection was forcibly closed by the remote host.
	#without the method tear down,all the windows open for testing the browser functionality remain open until the end and then all of them are closed
	#the result of the test is OK in both cases.
	#def tearDown(self):
	#	self.browser.close()





	
		