from tkinter import CASCADE

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.core.validators import integer_validator
from django.db import models


# -----------------------------------------------------------------------
# user start
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have a phone number!')
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        user = self.create_user(email, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=155, unique=False, null=True, blank=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=25, validators=[integer_validator], null=True, blank=True, unique=True)
    address = models.CharField(max_length=155, null=True, blank=True)
    # forget_password_token = models.CharField(max_length=100)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()


# user finish
# -----------------------------------------------------------------------------


class SocialLinksTypes(models.Model):
    title = models.CharField(max_length=100)
    icon = models.FileField(upload_to='images/icons/')

    def __str__(self):
        return self.title


class Instructor(models.Model):
    image = models.FileField(upload_to='images/instructors/')
    name = models.CharField(max_length=100)
    degree = models.CharField(max_length=150)
    bio = models.TextField()
    description = models.TextField()
    address = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class SocialLinks(models.Model):
    user = models.ForeignKey(to=Instructor,
                             on_delete=models.CASCADE,
                             related_name='user')
    type = models.ForeignKey(to=SocialLinksTypes,
                             on_delete=models.CASCADE,
                             related_name='sociallink')
    link = models.CharField(max_length=100)


# -----------------------------------------------------------------------------
# course start
class CourseCategory(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    icon = models.FileField(upload_to='images/icons/')

    def __str__(self):
        return self.title


class Course(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/course_images/')
    price = models.PositiveIntegerField()
    category = models.ForeignKey(to=CourseCategory,
                                 on_delete=models.CASCADE,
                                 related_name='categories')
    instructor = models.ForeignKey(to=Instructor,
                                   on_delete=models.CASCADE,
                                   related_name='instructor')
    duration = models.PositiveIntegerField()
    start = models.DateTimeField()
    main_description = models.TextField()
    benefits_description = models.TextField()
    finish_description = models.TextField()
    mini_review = models.CharField(max_length=200)
    discount_percentage = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


# course finish
# -------------------------------------------------------------------------------
# Blog start
# class Blog(models.Model):
#     pass
#

# Blog Finish
# ---------------------------------------------------------------------------------
# Comment Section

class CourseComment(models.Model):
    user = models.ForeignKey(to=User,
                             on_delete=models.CASCADE,
                             related_name='commenter')
    course = models.ForeignKey(to=Course,
                               on_delete=models.CASCADE,
                               related_name='course')
    comment = models.TextField()


class AboutBanner(models.Model):
    image = models.ImageField(upload_to='images/banner/')
    title = models.CharField(max_length=100)
    description = models.TextField()
    featureicon1 = models.ImageField(upload_to='images/aboutbanner')
    featureicon2 = models.ImageField(upload_to='images/aboutbanner')
    featureicon3 = models.ImageField(upload_to='images/aboutbanner')
    featuretext1 = models.TextField()
    featuretext2 = models.TextField()
    featuretext3 = models.TextField()


class Awards(models.Model):
    instructor = models.ForeignKey(to=Instructor,
                                   on_delete=models.CASCADE,
                                   related_name='awardOwner')
    title = models.CharField(max_length=100)
    description = models.TextField
    icon = models.ImageField(upload_to='images/awards/')


class Languages(models.Model):
    instructor = models.ForeignKey(to=Instructor,
                                   on_delete=models.CASCADE,
                                   related_name='skillOwner')
    language = models.CharField(max_length=100)
    percentage = models.PositiveIntegerField()


class Blog(models.Model):
    image = models.ImageField(upload_to='images/blog')
    title = models.CharField(max_length=100)
    data = models.DateField(auto_now_add=True)
    text = models.TextField()

    def __str__(self):
        return self.title


class BlogComment(models.Model):
    user = models.ForeignKey(to=User,
                             on_delete=models.CASCADE,
                             related_name='user')
    blog = models.ForeignKey(to=Blog,
                             on_delete=models.CASCADE,
                             related_name='course')
    comment = models.TextField()
    data = models.DateTimeField(auto_now_add=True)


# enrollment

class Enrolled(models.Model):
    course = models.ForeignKey(to=Course,
                               on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone_number = models.IntegerField()
