from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView

from Bekzod.forms import UserRegisterForm, UserLoginForm
from Bekzod.models import Post


# Create your views here.
class HomeView(TemplateView):
    template_name = 'blog/home.html'


class AboutView(TemplateView):
    template_name = 'blog/about.html'


class LoginView(View):
    def get(self, request):
        form = UserLoginForm()
        return render(request, 'blog/login.html', context={"form": form})

    def post(self, request):
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('Bekzod:home')
            else:
                form.add_error(None, 'Invalid username or password')
        return render(request, 'blog/login.html', context={"form": form})


class RegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'blog/register.html', context={"form": form})

    def post(self, request):
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('Bekzod:login')
        else:
            return render(request, 'blog/register.html', context={"form": form})


class PostConfirmDeleteView(TemplateView):
    template_name = 'blog/post_confirm_delete.html'


class PostDetailView(TemplateView):
    template_name = 'blog/post_detail.html'


class PostFormView(TemplateView):
    template_name = 'blog/post_form.html'


class UserPostsView(TemplateView):
    template_name = 'blog/user_posts.html'


def post_detail(request):
    post = Post.objects.all()
    context = {
        "post": post
    }
    return render(request, 'blog/post_form.html', context=context)
