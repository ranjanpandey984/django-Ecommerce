from django.shortcuts import render,redirect
from django.views.generic import View
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render

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
		paginator = Paginator(self.views['subcategories_product'], 1) #Show 25 contacts per page
		page_number = request.GET.get('page')
		self.views['page_obj'] = paginator.get_page(page_number)
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


def signup(request):
	if request.method == 'POST':
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		cpassword = request.POST['cpassword']

		if password == cpassword:
			if User.objects.filter(username = username).exists(): #User bhanney model django ma pailai huncha nabhako bhaye banauna parthyo afailey
				messages.error(request,'The Username is already taken.')
				return redirect('/signup')	
			elif User.objects.filter(email = email).exists(): 
				messages.error(request,'The Email ID is already taken.')
				return redirect('/signup')	
			else:
				user = User.objects.create_user(
					username = username,
					email = email,
					password = password,
				)
				user.save()
				messages.success(request,'You are registered successfully. ')
				return redirect('/signup')	
		else:
			messages.error(request,'2 passwords didnot match.')

	return render(request,'signup.html')




def add_to_cart(request):
	if request.method == 'POST':
		slug = request.POST['slug']
		quantity = request.POST['quantity']
		username = request.user.username
		items = Product.objects.filter(slug = slug)[0]
		price = Product.objects.get(slug = slug).price
		total = int(quantity) * int(price)

		if Cart.objects.filter(username = request.user.username,checkout = False, slug = slug).exists():
			qty = Cart.objects.get(username = request.user.username,checkout = False, slug = slug).quantity
			price = Product.objects.get(slug = slug).price
			quantity = int(quantity) + int(qty)
			total = int(price) * int(quantity)
			Cart.objects.filter(username = request.user.username,checkout = False, slug = slug).update(quantity = quantity, total = total)

		else:
			data = Cart.objects.create(
				slug = slug,
				quantity = quantity,
				username = username,
				items = items,
				total = total

				)
			data.save()
		return redirect ('/')


class CartView(BaseView):
	def get(self, request):
		self.views['my_cart'] = Cart.objects.filter(username = request.user.username,checkout = False)
		return render(request,'cart.html',self.views)


def remove_cart(request,slug):
	if Cart.objects.filter(username = request.user.username,checkout = False, slug = slug) .exists():
		Cart.objects.filter(username = request.user.username,checkout = False, slug = slug).delete()

	return redirect('/cart')




# ------------------------API------------------------------------------------------------------------------------------------


from rest_framework import routers, serializers, viewsets
from .serializers import *
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ItemSerializer


class ItemFilterView(generics.ListAPIView):
	queryset = Product.objects.all()
	serializer_class = ItemSerializer
	filter_backends = (DjangoFilterBackend,OrderingFilter,SearchFilter)
	filter_fields = ['id','price','labels','category','subcategory']
	ordering_fields = ['id','title','price']
	search_fields = ['title','description']

	
