import random
from django.core.cache import cache

def send_otp_to_email(email, user_obj):
    if cache.get(email):
        return False
    try:
        otp_to_send =random.randint(10000,99999)
        cache.set(email, otp_to_send , 120)
        user_obj.varification_otp =otp_to_send
        user_obj.save()
        return True
    except Exception as e:
        print(e)