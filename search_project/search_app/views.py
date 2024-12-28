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
)

from .models import Items, Review
from .searchItems import SearchItems


class ListView(LoginRequiredMixin, ListView):
    model = Items
    template_name = 'list.html'

class DetailView(DetailView):
    model = Items
    template_name = 'detail.html'


def index_view(request):
    return render(request,'index.html',)


class CreateReviewView(LoginRequiredMixin, CreateView):
    model = Review
    template_name = 'review_form.html'
    fields = ('item','text')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['item'] = Items.objects.get(pk=self.kwargs['item_id'])
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('detail', kwargs={'pk': self.object.item.id})
    
class SearchView(ListView):
    model = Items
    template_name = 'test.html'

    def get_queryset(self):
        instance = SearchItems()
        title = self.request.GET.get('title', None)
        genreId = self.request.GET.get('genreId', None)
        result = instance.search(title, genreId)
        print(result[0]['Items'][0]['Item']['itemName'])
        print(len(result[0]['Items']))
        print(result[1]['hits'][0]['name'])
        print(len(result[1]['hits']))
        return result