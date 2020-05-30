from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import DeleteView, DetailView,ListView,CreateView,UpdateView
from .models import AddProduct
from . import forms
from .forms import ProductModelForm, UserCreateForm
from .mixin import FormUserNeededMixin, UserOwnerMixin
# Create your views here.

class ProductCreateView(LoginRequiredMixin, FormUserNeededMixin, CreateView):
    form_class = ProductModelForm
    template_name = "product/create_view.html"
    success_url = "/"

    login_url = "/login/"

class ProductUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
    queryset = AddProduct.objects.all()
    form_class = ProductModelForm
    template_name = "product/update_view.html"
 #   success_url = '/'

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "product/delete_confirm.html"
    model = AddProduct
    success_url = reverse_lazy("product:list")
#retrieve
class ProductDetailView(DetailView):
    template_name="product/detail_view.html"
    queryset = AddProduct.objects.all()
    context_object_name = 'movie_list'

class ProductListView(ListView):
    context_object_name = 'movie_list'
    def get_queryset(self, *args, **kwargs):
        qs = AddProduct.objects.order_by('-updated')
        query = self.request.GET.get("q",None)
        if query is not None:
            qs = qs.filter(
                Q(movie_name__icontains=query) |
                Q(category__icontains=query) |
                Q(description__icontains=query)
            )
        return qs

    template_name="product/list_view.html"
    paginate_by = 16

class Hollywood(ListView):
    queryset = AddProduct.objects.filter(category__icontains='hollywood')
    context_object_name = 'movie_list'

    template_name="product/list_view.html"
    paginate_by = 16

class Bollywood(ListView):
    queryset = AddProduct.objects.filter(category__icontains='bollywood')
    context_object_name = 'movie_list'
    template_name="product/list_view.html"
    paginate_by = 16

class Tollywood(ListView):
    queryset = AddProduct.objects.filter(category__icontains='tollywood')
    context_object_name = 'movie_list'
    template_name="product/list_view.html"
    paginate_by = 16

class Animated(ListView):
    queryset = AddProduct.objects.filter(category__icontains='animated')
    context_object_name = 'movie_list'
    template_name="product/list_view.html"
    paginate_by = 16






class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'product/signup.html'