from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Photo, Category, Tag
from .forms import PhotoForm, PhotoSearchForm
import os

class PhotoListView(ListView):
    model = Photo
    template_name = "photo_list.html"
    context_object_name = "photo_list"
    paginate_by = 12  # ページネーション

    def get_queryset(self):
        queryset = Photo.objects.select_related('category', 'user').prefetch_related('tags')
        
        # 検索クエリ
        search_query = self.request.GET.get('search', '')
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) |
                Q(description__icontains=search_query) |
                Q(tags__name__icontains=search_query)
            ).distinct()
        
        # カテゴリフィルター
        category_id = self.request.GET.get('category', '')
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        
        # タグフィルター
        tag_id = self.request.GET.get('tag', '')
        if tag_id:
            queryset = queryset.filter(tags__id=tag_id)
        
        # 日付フィルター
        date_from = self.request.GET.get('date_from', '')
        date_to = self.request.GET.get('date_to', '')
        if date_from:
            queryset = queryset.filter(created_at__gte=date_from)
        if date_to:
            queryset = queryset.filter(created_at__lte=date_to)
        
        # 並び替え
        sort_by = self.request.GET.get('sort', '-created_at')
        queryset = queryset.order_by(sort_by)
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['tags'] = Tag.objects.all()
        context['search_form'] = PhotoSearchForm(self.request.GET)
        
        # 現在のフィルター条件を保持
        context['current_search'] = self.request.GET.get('search', '')
        context['current_category'] = self.request.GET.get('category', '')
        context['current_tag'] = self.request.GET.get('tag', '')
        context['current_sort'] = self.request.GET.get('sort', '-created_at')
        
        return context


class PhotoDetailView(DetailView):
    model = Photo
    template_name = "photo_detail.html"
    context_object_name = "photo"

    def get_queryset(self):
        return Photo.objects.select_related('category', 'user').prefetch_related('tags')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filename'] = os.path.basename(self.object.image.name)
        return context

class PhotoCreateView(LoginRequiredMixin, CreateView):
    model = Photo
    form_class = PhotoForm
    template_name = "photo_form.html"
    success_url = reverse_lazy('photoapp:photo_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PhotoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Photo
    form_class = PhotoForm
    template_name = "photo_form.html"
    success_url = reverse_lazy('photoapp:photo_list')

    def test_func(self):
        photo = self.get_object()
        return self.request.user == photo.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_update'] = True
        return context


class PhotoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Photo
    template_name = "photo_confirm_delete.html"
    success_url = reverse_lazy('photoapp:photo_list')

    def test_func(self):
        photo = self.get_object()
        return self.request.user == photo.user