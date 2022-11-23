from django.shortcuts import render
from .models import *
from django.views.generic import View
# Create your views here.
class BaseView(View):
    views = {}
    views['categories'] = Category.objects.all()

class HomeView(BaseView):
    def get(self,request):
        self.views
        self.views['sliders'] = Slider.objects.all()
        self.views['ads'] = Ad.objects.all()
        self.views['brands'] = Brand.objects.all()
        self.views['news'] = Product.objects.filter(labels = 'new')
        self.views['hots'] = Product.objects.filter(labels='hot')
        self.views['sales'] = Product.objects.filter(labels='sale')
        return render(request,'index.html',self.views)

class CategoryView(BaseView):
    def get(self,request,slug):
        self.views
        ids = Category.objects.get(slug = slug).id
        self.views['catproducts'] = Product.objects.filter(category_id = ids)
        return render(request, 'category.html', self.views)
class ProductDetailView(BaseView):
    def get(self,request,slug):
        self.views
        self.views['productdetails'] = Product.objects.filter(slug = slug)
        subcat_ids =Product.objects.get(slug = slug).subcategory_id
        self.views['related_products'] = Product.objects.filter(subcategory_id=subcat_ids)
        return render(request, 'product-detail.html', self.views)