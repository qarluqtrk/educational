from django.contrib.auth import login, logout
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect

from app.forms import RegisterForm, LoginForm, BlogCommentForm
from app.models import CourseCategory, Course, Instructor, Awards, Languages, Blog, BlogComment, AboutBanner


def index_view(request):
    blog = Blog.objects.order_by('data').all()[:3]
    about = AboutBanner.objects.first()
    instructors = Instructor.objects.all()
    categories = CourseCategory.objects.all()
    courses = Course.objects.all()[:6]
    if request.method == 'POST':
        text = request.POST['search']
        return redirect(f'/courses/?query={text}')
    return render(request=request,
                  template_name='app/index.html',
                  context={"categories": categories,
                           "courses": courses,
                           "about": about,
                           "instructors": instructors,
                           "blogs": blog})


def courses_view(request):
    categories = CourseCategory.objects.values('id', 'title')
    courses = Course.objects.all()
    paginator = Paginator(object_list=courses,
                          per_page=6)
    page_number = request.GET.get('page')
    course_list = paginator.get_page(number=page_number)

    query = request.GET.get('query', '')
    if query:
        course_list = Course.objects.filter(Q(title__icontains=query) |
                                            Q(category__id__icontains=query))
    return render(request=request,
                  template_name='app/courses.html',
                  context={"courses": course_list,
                           "categories": categories})


def course_view(request, course_id):
    course = Course.objects.filter(id=course_id).first()
    return render(request=request,
                  template_name='app/course.html',
                  context={"course": course})


def blog_view(request):
    blogs = Blog.objects.all()
    return render(request=request,
                  template_name='app/blog.html',
                  context={"blogs": blogs})


def blog_single_view(request, blog_id):
    blog = Blog.objects.filter(id=blog_id).first()
    comments = BlogComment.objects.order_by('data').all()

    if request.method == 'POST':
        form = BlogCommentForm(data=request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.blog = blog
            comment.save()
            return redirect(f'/blog-single/{blog.id}')
    form = BlogCommentForm
    return render(request=request,
                  template_name='app/blog-single.html',
                  context={"blog": blog,
                           "form": form,
                           "comments": comments})


def signup(request):
    if request.user.is_authenticated:
        return redirect("index")
    elif request.method == "POST":
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
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


def team_single(request, instructor_id):
    awards = Awards.objects.filter(instructor_id=instructor_id).all()
    if not awards:
        awards = 'None'
    language = Languages.objects.filter(instructor_id=instructor_id).all()
    if not language:
        language = 'None'
    instructor = Instructor.objects.filter(id=instructor_id).first()
    return render(request=request,
                  template_name='app/team-single.html',
                  context={"instructor": instructor,
                           "awards": awards,
                           "languages": language})


def results(request):
    return render(request=request,
                  template_name='app/results.html')
