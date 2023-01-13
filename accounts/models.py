from django.db import models
from base.models import Base
from django.conf import settings
# from django.contrib.auth.models import User
import os
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.core.mail import send_mail
from rest_framework.authtoken.models import Token


def get_upload_path(instance, filename):
    return os.path.join(str(instance.user.first_name),filename)

class User(AbstractUser):

    username = None
    profile_pic = models.ImageField(blank=True, upload_to=f"User/{get_upload_path}", null=True)
    email = models.EmailField(unique=True)
    is_email_varified = models.BooleanField(default=False)
    varification_otp = models.CharField(max_length=6, null=True, blank=True)
    # email_varification_token = models.CharField(max_length=200 , null=True , blank=True)
    forget_password_otp = models.CharField(max_length=200 , null=True, blank=True)
    # first_name = models.CharField(max_length=25)
    # last_name = models.CharField(max_length=25)
    USERNAME_FIELD ='email'
    REQUIRED_FIELDS=[]
    

    object = UserManager()

    

    def name(self):
        return f"{self.first_name}  {self.last_name}"

    def __str__(self) -> str:
        return self.email
        



@receiver(post_save, sender=User)
def send_otp(sender, instance, created, **kwargs):
    try:
        if created:
          Token.objects.create(user=instance)  

          
        otp = instance.varification_otp
        subject= "Email needs to be varified!"
        message = f'This is your OTP -{otp}.OTP is valid for 2 min.'
        print(message)
        recipient_list= [instance.email]
        email_from = settings.EMAIL_HOST_USER
        if otp:
          pass
        #   send_mail(subject=subject, message=message, 
        #   recipient_list=recipient_list, from_email=email_from, fail_silently=False)
          
    except Exception as e:
        print(e)