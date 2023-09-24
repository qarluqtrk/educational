from django.urls import path

from app.views import index_view, courses_view, course_view, blog_view, blog_single_view, signup, login_view, \
    logout_view

urlpatterns = [
    path('', index_view, name='index'),
    path('courses/', courses_view, name='courses'),
    path('course/', course_view, name='course'),
    path('blog/', blog_view, name='blog'),
    path('blog-single/', blog_single_view, name='blog-single'),

    # auth and sms verification
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('logout-page/', logout_view, name='logout'),
]
