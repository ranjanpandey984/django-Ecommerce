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
		return render(request,'index.html',self.views)