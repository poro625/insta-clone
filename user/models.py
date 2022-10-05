#user/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser



    
class UserModel(AbstractUser):
  
    class Meta:
        db_table = "my_user" # 테이블 이름
        
        
    email = models.EmailField(verbose_name = "email", max_length = 255, unique = True)
    username = models.CharField(max_length=30)
    nickname = models.CharField(max_length=50, blank=True)
    
    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = ['username']
    


# class profile(models.Model):
#     title = models.CharField(max_length=100)
#     pic = models.FileField(null=True, blank=True, upload_to="")
    
#     def __str__(self):
#         return self.title
    

