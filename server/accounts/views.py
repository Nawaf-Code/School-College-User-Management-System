import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import User
from rest_framework import generics
from .serializers import UserSerializer, VerifyAccountSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from .emails import send_otp



@csrf_exempt  # Temporarily disable CSRF protection for demonstration purposes
def check_email(request):
    if request.method == 'POST':  # Change the method to POST
        data = json.loads(request.body)
        email = data.get('email')
        if User.objects.filter(email=email).exists():
            return JsonResponse({'email_exists': True}, status=200)
        else:
            return JsonResponse({'email_exists': False}, status=200)
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)
    

@csrf_exempt 
def re_send_otp(request):
    if request.method == 'POST': 
        data = json.loads(request.body)
        email = data.get('email')
        send_otp(email)
        return JsonResponse({'is_sent': True}, status=200)
    else:
        return JsonResponse({'is_sent': False}, status=400)

class Register(APIView):

    def post(self, request):
        try:
           data = request.data

           userEmail = data.get('email')
           serializer_class = UserSerializer(data=data)
           if serializer_class.is_valid():
               user = User.objects.filter(email = userEmail)
               if not user.exists():
                  serializer_class.save()
                  is_sent = send_otp(userEmail)

                  return Response({
                        'status': 200,
                        'message': 'user created succefuly',
                        'data': serializer_class.data,
                        'is_sent': is_sent
                        })
               else:
                return Response({
                    'status': 400,
                    'message': 'the account is exists',
                    'data': serializer_class.errors,
                    'is_sent': False
                    })
               
               
           else:
               return Response({
                   'status': 400,
                   'message': 'something wrong',
                   'data': serializer_class.errors,
                   'is_sent': False
                   })
        except Exception as e:
            print(e)
            return Response({
                'status': 500,
                'message': 'An error occurred',
                'error': str(e),
                'is_sent': False
            }, status=500)
        

class VerifyOTP(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = VerifyAccountSerializer(data=data)

            if serializer.is_valid():
               email = serializer.data['email']
               code = serializer.data['code']

               user = User.objects.get(email=email)

               if user.otp != code or user.is_expired():
                   return Response({
                    'status': 400,
                    'is_valid': False
                    })
               else:
                   user.is_active = True
                   user.save()

               return Response({
                   'status': 200,
                   'is_valid': True
                   })
            else:
                return Response({
                    'status': 400,
                   'is_valid': False
                    })

        except Exception as e:
            print(e)
            return Response({
                'status': 500,
                'message': 'An error occurred',
                'is_valid': False,
                'error': str(e)
            }, status=500)






        

    




