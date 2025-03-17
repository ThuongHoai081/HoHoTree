from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from ..users.serializers import UserSerializer
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import render

User = get_user_model()

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            #Tạo một token để xác thực email.
            token = default_token_generator.make_token(user)
            print("token" + token)
            # Mã hoá user
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            print("uid" + uid)
            activation_link = f"http://localhost:8000/api/auth/activate/{uid}/{token}/"
            print("activation_link" + activation_link)
            send_mail(
                'Xác nhận tài khoản',
                f'Nhấp vào liên kết sau để xác nhận tài khoản của bạn: {activation_link}',
                settings.EMAIL_HOST_USER,
                [user.email],
                fail_silently=False,
            )
            return Response({'message': 'Vui lòng kiểm tra email để xác thực tài khoản.'}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#Xử lý kích hoạt tài khoản 
class ActivateUserView(APIView):
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            #Tìm user trong database
            user = get_object_or_404(User, pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        #Kiểm tra token và kích hoạt tài khoản
        if user and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            context = {
                'message': 'Tài khoản của bạn đã được kích hoạt thành công!',
                'description': 'Bạn có thể đăng nhập và sử dụng hệ thống.',
            }
            
            return render(request, 'activation_success.html', context=context)

        context = {
            'message': 'Liên kết không hợp lệ hoặc đã hết hạn!',
            'description': 'Liên kết kích hoạt của bạn đã hết hạn hoặc không hợp lệ. Vui lòng đăng ký lại.',
        }
        return render(request, 'activation_success.html', context=context)
