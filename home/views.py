from django.shortcuts import render
from django.views.generic import View
# Create your views here.

class BaseView(View):
	view = {}



class HomeView(BaseView):
	def get(self,request):

		return render(request,'index.html')