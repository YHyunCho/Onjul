from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Board(models.Model) :
  email = models.EmailField(max_length=128)
  user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)