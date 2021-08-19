from django.db import models
from django.urls import reverse
# Create your models here.


class Category(models.Model):
	title = models.CharField(max_length = 400)
	slug = models.CharField(max_length = 500, unique = True) #Slug bhaneko ID jastai primary key 
	description = models.TextField()

	def __str__(self):
		return self.title 


class SubCategory(models.Model):
	title = models.CharField(max_length = 400)
	category = models.ForeignKey(Category, on_delete = models.CASCADE)
	slug = models.CharField(max_length = 500, unique = True) 
	description = models.TextField()

	def __str__(self):
		return self.title 

	def get_url(self):
		return reverse("home:subcategory",kwargs = {'slug':self.slug})


class Slider(models.Model):
	title = models.CharField(max_length = 400)
	slug = models.CharField(max_length = 500, unique = True) 
	description = models.TextField()
	image = models.ImageField(upload_to = 'media')
	rank = models.IntegerField()
	status = models.CharField(max_length = 100, choices = (('active','active'),('','inactive')))
	# first active bhaneko database ko lagi value ho and pachadiko active dropdown ko value ho jun frontend ma click huncha

	def __str__(self):
		return self.title


class Brand(models.Model):
	title = models.CharField(max_length = 400)
	slug = models.CharField(max_length = 500, unique = True) 
	description = models.TextField()

	def __str__(self):
		return self.title 

	def get_url(self):
		return reverse("home:brand",kwargs = {'slug':self.slug})


class Product(models.Model):
	title = models.CharField(max_length = 500)
	slug = models.CharField(max_length = 500, default = "", blank = True) 
	price = models.IntegerField()
	discounted_price = models.IntegerField()
	status = models.CharField(max_length = 100, choices = (('active','active'),('','inactive')))
	image = models.ImageField(upload_to = 'media')
	description = models.TextField(blank = True)
	labels = models.CharField(max_length = 100, choices = (('new','new'),('hot','hot'),('sale','sale')))
	category = models.ForeignKey(Category, on_delete = models.CASCADE)
	subcategory = models.ForeignKey(SubCategory, on_delete = models.CASCADE)
	brand = models.ForeignKey(Brand, on_delete = models.CASCADE, null = True)
	stock = models.CharField(max_length = 100, choices = (('In Stock','In Stock'),('Out of Stock','Out of Stock')))

	def __str__(self):
		return self.title
	
	def get_url(self):
		return reverse("home:product",kwargs = {'slug':self.slug})




class Cart(models.Model):
	username = models.CharField(max_length = 300)
	slug = models.CharField(max_length = 300)
	quantity = models.IntegerField(default = 1)
	date = models.DateTimeField(auto_now_add = True)
	checkout = models.BooleanField(default = False)
	items = models.ForeignKey(Product, on_delete = models.CASCADE, null = True)
	total = models.IntegerField(default = 0)

	def __str__(self):
		return self.username

	def get_url(self):
		return reverse("home:remove-cart",kwargs = {'slug':self.slug})