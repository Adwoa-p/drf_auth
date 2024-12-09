# this allows us to map user json objects/inputs from apis to data in our db
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ['id', 'username', 'password', 'email']


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email','password']
        extra_kwargs = {'password':{'write_only': True}}

        def create(self,  validated_data):
            user = User.objects.create_user(validated_data['username'],validated_data['password'],validated_data['email'] )       

            return user  