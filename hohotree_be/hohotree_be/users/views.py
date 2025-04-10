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
            fullname = serializer.validated_data['full_name']

            # Đăng ký user trên Supabase
            response = supabase.auth.sign_up({
                "full_name": fullname,
                "email": email,
                "password": password
            })

            if not response.user:
                return Response(
                    {'error': 'Đăng ký thất bại. Vui lòng kiểm tra lại thông tin hoặc email đã tồn tại.'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            return Response(
                {'message': 'Vui lòng kiểm tra email để xác thực tài khoản.', "status": "201"},
                status=status.HTTP_201_CREATED
            )

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
        if not response.session:
                return Response({'error': 'Đăng nhập thất bại. Vui lòng kiểm tra lại email và mật khẩu.'},
                                status=status.HTTP_400_BAD_REQUEST)

        # Lưu thông tin người dùng vào session
        return Response({
            "access_token": response.session.access_token,
            "refresh_token": response.session.refresh_token
        }, status=status.HTTP_200_OK)


class SupabaseRefreshTokenView(APIView):
    def post(self, request):
        refresh_token = request.data.get("refresh_token")

        # Gọi API refresh token Supabase
        response = supabase.auth.refresh_session({"refresh_token": refresh_token})

        if response.error:
            return Response({'error': response.error.message}, status=status.HTTP_400_BAD_REQUEST)

        return Response({
            "access_token": response.session.access_token,
            "refresh_token": response.session.refresh_token
        }, status=status.HTTP_200_OK)
