from django.contrib import admin

from app.models import User, Instructor, CourseCategory, Course, CourseComment, SocialLinks, SocialLinksTypes, Awards, \
    Languages, Blog, AboutBanner


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name')


admin.site.register(User, UserAdmin)
admin.site.register([Instructor,
                     CourseCategory,
                     Course,
                     CourseComment,
                     SocialLinks,
                     SocialLinksTypes,
                     Awards,
                     Languages,
                     Blog,
                     AboutBanner
                     ])
