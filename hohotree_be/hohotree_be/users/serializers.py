import re
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.core.validators import EmailValidator

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=150, write_only=True)

    class Meta:
        model = User
        fields = ("id", "full_name", "email", "password")

    def validate_email(self, value):
        # Kiểm tra email đã tồn tại trong cơ sở dữ liệu
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email đã được sử dụng")

        # Kiểm tra định dạng email bằng EmailValidator của Django
        validator = EmailValidator()
        try:
            validator(value)
        except Exception:
            raise serializers.ValidationError("Email có định dạng không hợp lệ")

        return value

    def validate_password(self, value):
        # Kiểm tra mật khẩu có ít nhất 8 ký tự, chứa chữ cái, số và ký tự đặc biệt
        pattern = r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$"
        if not re.match(pattern, value):
            raise serializers.ValidationError(
                "Mật khẩu phải dài ít nhất 8 ký tự, bao gồm ít nhất một chữ cái, một số và một ký tự đặc biệt."
            )
        return value

    def create(self, validated_data):
        user = User.objects.create_user(
            full_name=validated_data['full_name'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        user.is_active = False
        user.save()

        return user
