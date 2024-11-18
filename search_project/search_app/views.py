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

from .models import Book, Review, Like


class ListBookView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'book_list.html'

class DetailBookView(DetailView):
    model = Book
    template_name = 'book_detail.html'


class CreateBookView(LoginRequiredMixin, CreateView):
    model = Book
    template_name = 'book_create.html'
    fields = ('title', 'text', 'category', 'thumbnail' ,'start', 'end')
    success_url = reverse_lazy('list-book')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class DeleteBookView(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = 'book_delete.html'
    success_url = reverse_lazy('list-book')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        if obj.user != self.request.user:
            raise PermissionDenied

        return obj


class UpdateBookView(LoginRequiredMixin, UpdateView):
    model = Book
    template_name = 'book_update.html'
    fields = ('title', 'text', 'category', 'thumbnail')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        if obj.user != self.request.user:
            raise PermissionDenied

        return obj

    def get_success_url(self):
        return reverse('detail-book', kwargs={'pk': self.object.id})


def index_view(request):
    order = ('start',)
    query = Book.objects.all().order_by(*order)
    first = True
    data = []
    month = []
    for q in query:
        if first:
            first = False
            month.append(q)
            prev=q.start.strftime("%Y-%m")
        else:
            if q.start.strftime("%Y-%m") != prev:
                data.append(month)
                month = []
                month.append(q)
                prev = q.start.strftime("%Y-%m")
            else:
                month.append(q)
    data.append(month)
    return render(
        request,
        'index.html',
        {
            'data': data,
        }
    )


class CreateReviewView(LoginRequiredMixin, CreateView):
    model = Review
    template_name = 'review_form.html'
    fields = ('book','text')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book'] = Book.objects.get(pk=self.kwargs['book_id'])
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('detail-book', kwargs={'pk': self.object.book.id})
    
class SearchView(ListView):
    model = Book
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
    model = Book
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