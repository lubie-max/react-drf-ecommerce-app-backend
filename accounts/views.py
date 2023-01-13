from django.shortcuts import render,HttpResponse
from django.views import View
from .models import User
from django.contrib.auth import authenticate
from rest_framework import status
from django.contrib.auth.views import LogoutView
# //
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .helpers import * 
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated



def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class RegisterView(APIView):

    def post(self, request, format=None):
        try:
         
            serializer = RegisterUserSerializer(data=request.data)
            token = None
            if  serializer.is_valid():
                user = serializer.save()
                token = get_tokens_for_user(user)
                print(serializer.data , token)
                return Response({'status':200 , 'msg':'Otp has been sent to your email.', "Token":token})

            return Response({'status':403, 'error':serializer.errors})

            
        except Exception as e:
            print(e)
            return Response({'status':404 , 'msg':e})



class UserLoginView(APIView):

    def post(self, request, format=None):
        try:
            serializer = LoginUserSerializer(data=request.data)
            if serializer.is_valid() :
                email = serializer.data.get('email')
                password = serializer.data.get('password')

                user = authenticate(email=email, password=password)
                token = get_tokens_for_user(user)
                if user:
                    return Response({'token': token }, status.HTTP_200_OK)

           
            return Response({'error':"unauthorized login."},  status=status.HTTP_401_UNAUTHORIZED )

        except Exception as e:
            print(e)
            return Response({'error':e})


class UserProfileView(APIView):
    # permission_classes= [IsAuthenticated]
    permission_classes = [IsAuthenticated]
    def get(self, request,*args, **kwargs):
        try:
            serializer = ProfileSerializer(request.user)
            return Response({'data': serializer.data}, status.HTTP_200_OK)

        except Exception as e:
            print(e)

class  ChangeUserPasswordView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            serializer = ChangePasswordSerializer(data= request.data, context={'user': request.user})
            if serializer.is_valid() :

                return Response({'Message': "Password has been changed!"}, status.HTTP_200_OK)

            return Response({'error':serializer.errors},  status=status.HTTP_401_UNAUTHORIZED )
            

        except Exception as e:
            print(e)



class UserLogout(LogoutView, APIView):
    def post(self, request,*args, **kwargs):
        try:
            response = super().post(request, *args, **kwargs)
            print(response)
            return Response({'success': 'Successfully logged out'}, status=status.HTTP_200_OK)
            
        except Exception as e:
            print(e)
            return Response({'error':e})



class VarifyingEmailByOtp(APIView):
    def post(self, request):
        try:
            data = request.data
            user_otp = data.get('otp')
            user_obj = User.objects.get(email= data.get('email'))
            
            if user_obj.varification_otp  == user_otp:

                user_obj.is_email_varified = True
                user_obj.save()
                return Response({'success': 'Successfully varified the email.'}, status=status.HTTP_200_OK)

            return Response({'msg': 'Unable to varified.'}, status=status.HTTP_401_UNAUTHORIZED)

        except Exception as e:
            print(e)
            return Response({'error':e})



    def patch(self, request):
        try:
            data = request.data

            email = data.get('email')
            user =User.objects.filter(email = email)
            if not user.exists():
                return Response({'msg': 'invalid request.'})

            send_otp_to_email(data.get('email'), user_obj=user[0])
            return Response({'msg': f'Otp has been sent to your email.'})

        except Exception as e:
            print(e)
            return Response({'error':e})
