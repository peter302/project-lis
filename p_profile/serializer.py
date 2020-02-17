from rest_framework import serializers
from .models import Profile, Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title','image', 'description', 'user', 'date_posted', 'link', 'country']
