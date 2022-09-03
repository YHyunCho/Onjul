from django.db import models
from django.contrib.auth.models import User
import os

# Create your models here.

class Tag(models.Model) :
  name = models.CharField(max_length=50)
  slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

  def __str__(self) :
    return self.name

  def get_absolute_url(self) :
    return f'/sharing/tag/{self.slug}/'

class Post(models.Model) :
  title = models.CharField(max_length=30)
  content = models.TextField()

  head_image = models.ImageField(upload_to='sharing/image/%Y/%m/%d', blank=True)
  created_at = models.DateTimeField(auto_now_add=True)  # 작성시간 저장
  updated_at = models.DateTimeField(auto_now=True)      # 수정시간 저장
  
  author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL) # set_null = 작성자가 삭제되어도 글은 삭제 x

  tags = models.ManyToManyField(Tag, blank=True)

  def __str__(self):
    return f'[{self.pk}]{self.title} :: {self.author}' # 리스트에서 포스트 제목 나타나게 하기

  def get_absolute_url(self):
    return f'/sharing/{self.pk}/'

class Photo(models.Model) :
  post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
  image = models.ImageField(upload_to='image/', blank=True, null=True)