# this allows us to map user json objects/inputs from apis to data in our db
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = [ 'id','first_name','last_name', 'username', 'email', 'password', 'phone_number'] 


