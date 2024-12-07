from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from django.db.models import Avg
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,
)

from .models import Product, Review, Like


class ListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'list.html'

class DetailView(DetailView):
    model = Product
    template_name = 'detail.html'


class CreateItemView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'create.html'
    fields = ('title', 'text', 'category', 'thumbnail' ,'start', 'end')
    success_url = reverse_lazy('list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class DeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'delete.html'
    success_url = reverse_lazy('list')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        if obj.user != self.request.user:
            raise PermissionDenied

        return obj


class UpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    template_name = 'update.html'
    fields = ('title', 'text', 'category', 'thumbnail')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        if obj.user != self.request.user:
            raise PermissionDenied

        return obj

    def get_success_url(self):
        return reverse('detail', kwargs={'pk': self.object.id})


def index_view(request):
    return render(request,'index.html',)


class CreateReviewView(LoginRequiredMixin, CreateView):
    model = Review
    template_name = 'review_form.html'
    fields = ('product','text')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = Product.objects.get(pk=self.kwargs['product_id'])
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('detail', kwargs={'pk': self.object.product.id})
    
class SearchView(ListView):
    model = Product
    template_name = 'search.html'

    def get_queryset(self):
        query = super().get_queryset()
        title = self.request.GET.get('title', None)
        category = self.request.GET.get('category',None)
        if title:
            query = query.filter(title__icontains=title)
        elif category:
            query= query.filter(category__iexact = category)
        return query
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = self.request.GET.get('category', '')
        return context

class LikeView(ListView):
    model = Product
    template_name = 'acp.html'


    def get_queryset(self):
        query = super().get_queryset()
        title = self.request.GET.get('title', None)
        if title:
            query = query.filter(title__icontains=title)
        return query
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.request.GET.get('title', '')
        return context
    
class AcpView(ListView):
    model = Like
    template_name = 'acp.html'