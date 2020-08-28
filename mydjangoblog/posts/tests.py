from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from django.shortcuts import reverse
from .models import Post
# Create your tests here.

class HomePageTests(SimpleTestCase):
	############# STATUS CODE TEST ####################
	def test_home_status_code(self):
		response = self.client.get('/homepage/')
		self.assertEquals(response.status_code,200)
	############# URLS TEST ###################
	def test_home_url_name(self):
		response = self.client.get(reverse('homepage'))
		self.assertEquals(response.status_code,200)
	############# TEMPLATE TEST(VIEWS) ###############
	def test_correct_home_template(self):
		response = self.client.get(reverse('homepage'))
		self.assertEquals(response.status_code,200)
		self.assertTemplateUsed(response, 'homepage.html')
		

class PortfolioTests(SimpleTestCase):
	############# STATUS CODE TEST####################
	def test_Portfolio_status_code(self):
		response = self.client.get('/resume/')
		self.assertEquals(response.status_code,200)
	############# URLS TEST ###################
	def test_portfolio_url_name(self):
		response = self.client.get(reverse('resume'))
		self.assertEquals(response.status_code,200)
	############# TEMPLATE TEST ###############
	def test_correct_portfolio_template(self):
		response = self.client.get(reverse('resume'))
		self.assertEquals(response.status_code,200)
		self.assertTemplateUsed(response, 'resume.html')


class ContactMePageTests(SimpleTestCase):
	############# STATUS CODE TEST####################
	def test_contactme_status_code(self):
		response = self.client.get('/contactme/')
		self.assertEquals(response.status_code,200)
	############# URLS TEST ###################
	def test_contactme_url_name(self):
		response = self.client.get(reverse('contactme'))
		self.assertEquals(response.status_code,200)
	############# TEMPLATE TEST ###############
	def test_correct_contacme_template(self):
		response = self.client.get(reverse('contactme'))
		self.assertEquals(response.status_code,200)
		self.assertTemplateUsed(response, 'contactme.html')


class ProjectsPageTests(SimpleTestCase):
	############# STATUS CODE TEST####################
	def test_projects_status_code(self):
		response = self.client.get('/projects/')
		self.assertEquals(response.status_code,200)
	############# URLS TEST ###################
	def test_projects_url_name(self):
		response = self.client.get(reverse('projects'))
		self.assertEquals(response.status_code,200)
		############# TEMPLATE TEST ###############
	def test_correct_projects_template(self):
		response = self.client.get(reverse('projects'))
		self.assertEquals(response.status_code,200)
		self.assertTemplateUsed(response, 'projects.html')


class EducationPageTests(SimpleTestCase):
	############# STATUS CODE TEST####################
	def test_education_status_code(self):
		response = self.client.get('/education/')
		self.assertEquals(response.status_code,200)
	############# URLS TEST ###################
	def test_education_url_name(self):
		response = self.client.get(reverse('education'))
		self.assertEquals(response.status_code,200)
	############# TEMPLATE TEST ###############
	def test_correct_education_template(self):
		response = self.client.get(reverse('education'))
		self.assertEquals(response.status_code,200)
		self.assertTemplateUsed(response, 'education.html')


class PostTests(TestCase):
	
	def setUp(cls):
		Post.objects.create(title='this is a test')

	def test_text(self):
		post = Post.objects.get(id=1)
		expected_post_title = post.title
		self.assertEquals(expected_post_title, 'this is a test')

	def test_post_list_view(self):
		response = self.client.get('//')
		self.assertEquals(response.status_code, 200)
		self.assertContains(response, 'this is a test')
		self.assertTemplateUsed(response, 'base.html')

#
#lass TestModels(TestCase):
#	def setUp(self):
#		self.post = Post.objects.create(
#			title= __str__(self),
#		)
###
##	def post_has_startslug(self):
#		self.assertEquals(self.post.slug, __str__(self))
