from django.db import models

# Create your models here.

class SharingList(models.Model) :
  title = models.CharField(max_length=30)
  content = models.TextField()

  created_at = models.DateTimeField(auto_now_add=True)# 작성시간 저장
  updated_at = models.DateTimeField(auto_now=True)    # 수정시간 저장

  def __str__(self):
    return f'[{self.pk}]{self.title}' # 리스트에서 포스트 제목 나타나게 하기