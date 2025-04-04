# from django.contrib.auth import get_user_model
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework import status
# from ..users.serializers import UserSerializer
# from django.core.mail import send_mail
# from django.conf import settings
# from django.shortcuts import get_object_or_404
# from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# from django.utils.encoding import force_bytes, force_str
# from django.contrib.auth.tokens import default_token_generator
# from django.shortcuts import render

# User = get_user_model()

# class RegisterView(APIView):
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             #Tạo một token để xác thực email.
#             token = default_token_generator.make_token(user)
#             print("token" + token)
#             # Mã hoá user
#             uid = urlsafe_base64_encode(force_bytes(user.pk))
#             print("uid" + uid)
#             activation_link = f"http://localhost:8000/api/auth/activate/{uid}/{token}/"
#             print("activation_link" + activation_link)
#             send_mail(
#                 'Xác nhận tài khoản',
#                 f'Nhấp vào liên kết sau để xác nhận tài khoản của bạn: {activation_link}',
#                 settings.EMAIL_HOST_USER,
#                 [user.email],
#                 fail_silently=False,
#             )
#             return Response({'message': 'Vui lòng kiểm tra email để xác thực tài khoản.'}, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# #Xử lý kích hoạt tài khoản 
# class ActivateUserView(APIView):
#     def get(self, request, uidb64, token):
#         try:
#             uid = force_str(urlsafe_base64_decode(uidb64))
#             #Tìm user trong database
#             user = get_object_or_404(User, pk=uid)
#         except (TypeError, ValueError, OverflowError, User.DoesNotExist):
#             user = None
#         #Kiểm tra token và kích hoạt tài khoản
#         if user and default_token_generator.check_token(user, token):
#             user.is_active = True
#             user.save()
#             context = {
#                 'message': 'Tài khoản của bạn đã được kích hoạt thành công!',
#                 'description': 'Bạn có thể đăng nhập và sử dụng hệ thống.',
#             }
            
#             return render(request, 'activation_success.html', context=context)

#         context = {
#             'message': 'Liên kết không hợp lệ hoặc đã hết hạn!',
#             'description': 'Liên kết kích hoạt của bạn đã hết hạn hoặc không hợp lệ. Vui lòng đăng ký lại.',
#         }
#         return render(request, 'activation_success.html', context=context)

from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from ..users.serializers import UserSerializer
from django.shortcuts import render
from supabase import create_client
import jwt

# Kết nối Supabase
SUPABASE_URL = settings.SUPABASE_URL
SUPABASE_KEY = settings.SUPABASE_KEY
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']

            # Đăng ký user trên Supabase
            response = supabase.auth.sign_up({
                "email": email,
                "password": password
            })

            if response.get("error"):
                return Response({'error': response["error"]["message"]}, status=status.HTTP_400_BAD_REQUEST)

            return Response({'message': 'Vui lòng kiểm tra email để xác thực tài khoản.'}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class ActivateUserView(APIView):
    def get(self, request, token):
        try:
            # Giải mã token từ Supabase
            decoded_token = jwt.decode(token, options={"verify_signature": False})
            user_email = decoded_token.get("email")

            if not user_email:
                raise ValueError("Token không hợp lệ.")

            return render(request, 'activation_success.html', {
                'message': 'Tài khoản của bạn đã được kích hoạt thành công!',
                'description': 'Bạn có thể đăng nhập và sử dụng hệ thống.'
            })
        except jwt.ExpiredSignatureError:
            return render(request, 'activation_success.html', {
                'message': 'Liên kết không hợp lệ hoặc đã hết hạn!',
                'description': 'Vui lòng đăng ký lại.'
            })

class SupabaseLoginView(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        # Gọi API đăng nhập Supabase
        response = supabase.auth.sign_in_with_password({
            "email": email,
            "password": password
        })

        if response.get("error"):
            return Response({'error': response["error"]["message"]}, status=status.HTTP_400_BAD_REQUEST)

        return Response({
            "access_token": response["session"]["access_token"],
            "refresh_token": response["session"]["refresh_token"]
        }, status=status.HTTP_200_OK)


class SupabaseRefreshTokenView(APIView):
    def post(self, request):
        refresh_token = request.data.get("refresh_token")

        # Gọi API refresh token Supabase
        response = supabase.auth.refresh_session(refresh_token)

        if response.get("error"):
            return Response({'error': response["error"]["message"]}, status=status.HTTP_400_BAD_REQUEST)

        return Response({
            "access_token": response["session"]["access_token"],
            "refresh_token": response["session"]["refresh_token"]
        }, status=status.HTTP_200_OK)