from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from .models import *
from .forms import NewPostCreate, ResponseCreate
from .filters import RespFilter


class PostView(ListView):
    model = Post
    ordering = '-date'
    template_name = 'main.html'
    context_object_name = 'post'
    paginate_by = 5


class DetailPost(DetailView):
    model = Post
    template_name = 'detail.html'
    context_object_name = 'fullpost'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['response'] = UserResponse.objects.filter(post_id=self.kwargs['pk'])
        context['filterset'] = self.filterset
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = RespFilter(self.request.GET, queryset)
        return self.filterset.qs

class PostCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('main.add_post')
    form_class = NewPostCreate
    model = Post
    template_name = 'post_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        return super().form_valid(form)


class PostUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('main.change_post')
    form_class = NewPostCreate
    model = Post
    template_name = 'post_edit.html'


class PostDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('main.delete_post')
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('allpost')


class NewResponse(PermissionRequiredMixin, CreateView):
    permission_required = ('main.add_userresponse')
    form_class = ResponseCreate
    model = UserResponse
    template_name = 'response.html'
    success_url = reverse_lazy('allpost')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        post = Post.objects.get(id=kwargs['pk'])
        if form.is_valid():
            resp = form.save(commit=False)
            resp.author = request.user
            resp.post = post
            resp.save()
            return self.form_valid(form)


def responsedelete(request, pk):
    response = UserResponse.objects.get(id=pk)
    response.delete()

    return redirect('allpost')


def accept(request, pk):
    response = UserResponse.objects.get(id=pk)
    response.status = True
    response.save()

    return redirect('allpost')


def denied(request, pk):
    response = UserResponse.objects.get(id=pk)
    response.status = False
    response.save()

    return redirect('allpost')