from rest_framework import serializers
from django.contrib.auth.models import User
# này chắc hoài hiểu nhờ.
# à bành hoài nhớ chạy python manage.py migrate cấu hình data giống ở loacl.py nha bà 
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        user.is_active = False 
        user.save()
        return user