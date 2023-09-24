from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from app.forms import RegisterForm, LoginForm


def index_view(request):
    return render(request=request,
                  template_name='app/index.html')


def courses_view(request):
    return render(request=request,
                  template_name='app/courses.html')


def course_view(request):
    return render(request=request,
                  template_name='app/course.html')


def blog_view(request):
    return render(request=request,
                  template_name='app/blog.html')


def blog_single_view(request):
    return render(request=request,
                  template_name='app/blog-single.html')


def signup(request):
    if request.user.is_authenticated:
        return redirect("index")
    elif request.method == "POST":
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = RegisterForm()
    return render(request=request,
                  template_name='app/signup.html',
                  context={'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect("index")
    elif request.method == "POST":
        form = LoginForm(request=request,
                         data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request=request,
                  user=user)

            return redirect('index')

    form = LoginForm()
    return render(request=request,
                  template_name='app/login.html',
                  context={"form": form})


def logout_view(request):
    logout(request=request)
    return redirect('index')
