from django.shortcuts import render
from django.views.generic import View
from .models import *

# Create your views here.

class BaseView(View): # parameter ko view chahi generic view ho
	views = {}



class HomeView(BaseView):
	def get(self,request):
		self.views['sliders'] = Slider.objects.all()
		self.views['categories'] = Category.objects.all()
		self.views['subcategories'] = SubCategory.objects.all()
		self.views['items'] = Product.objects.filter(status = 'active')
		self.views['brands'] = Brand.objects.all()
		return render(request,'index.html',self.views)


class ProductDetailView(BaseView):
	def get(self,request,slug):
		self.views['detail_product'] = Product.objects.filter(slug = slug)
		return render (request,'product-details.html',self.views)



class SubCategoryViews(BaseView):
	def get(self,request,slug):
		id = SubCategory.objects.get(slug = slug).id
		self.views['subcategories_product'] = Product.objects.filter(subcategory_id = id)
		return render(request,'subcategory.html',self.views)



class BrandViews(BaseView):
	def get(self,request,slug):
		id = Brand.objects.get(slug = slug).id
		self.views['brands_product'] = Product.objects.filter(brand_id = id)
		return render(request,'brand.html',self.views)
		

class Search(BaseView):
	def get(self,request):
		query = request.GET.get('query', None)
		if not query:
			return redirect('/')
		self.views['search_query'] = Product.objects.filter(title__icontains = query)  #icontains bhaneko search gareko sanga mildo juldo data
		return render(request,'search.html',self.views)