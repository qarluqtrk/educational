from django.urls import path

from app.views import index_view, courses_view, course_view, blog_view, blog_single_view, signup, login_view, \
    logout_view, team_single, results

urlpatterns = [
    path('', index_view, name='index'),
    path('courses/', courses_view, name='courses'),
    path('course/<int:course_id>', course_view, name='course'),
    path('blog/', blog_view, name='blog'),
    path('blog-single/<int:blog_id>', blog_single_view, name='blog-single'),

    path('team/<int:instructor_id>', team_single, name='team-single'),

    # auth and sms verification
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('logout-page/', logout_view, name='logout'),

    path('results/', results, name='results')
]
