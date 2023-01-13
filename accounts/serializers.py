from rest_framework import serializers
from .models import User
from .helpers import send_otp_to_email


class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =['email', 'password','first_name', 'last_name']


    extra_kwargs ={
        'password':{'write_only':True}
    }
    
    def create(self, validated_data):
            user = User.objects.create(email= validated_data['email'],first_name= validated_data['first_name'], last_name= validated_data['last_name'])
            email= validated_data['email']
            # self.normalize_email(email)
            user.set_password(validated_data['password'])
            user.save()
            send_otp_to_email(user.email, user)
            return user




class LoginUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length= 255)
 
    class Meta:
        model = User
        fields =['email', 'password']


class ProfileSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length= 255)
 
    class Meta:
        model = User
        fields =['email', 'first_name','last_name','profile_pic']


class ChangePasswordSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(max_length=255, style={'input_type':'password'}, write_only= True)
    password2 = serializers.CharField(max_length=255, style={'input_type':'password'}, write_only= True)
    class Meta:
        model = User
        fields =['password', 'password2']

    def validate(self, data):
        password =data.get('password')
        password2 =data.get('password2')
        user = self.context.get('user')
        if password != password2:
            raise serializers.ValidationError("Password and confirm password are not same!")
        user.set_password(password)
        user.save()
        return super().validate(data)
