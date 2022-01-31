from rest_framework import serializers
from theblog.models import Post, CustomUser
from django.contrib.auth.models import User
from django.conf import settings


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
            "avatar"
        )


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    like_count = serializers.IntegerField()

    class Meta:
        model = Post
        fields = (
            "title",
            "slug",
            "header_image",
            "title_tag",
            "author",
            "body",
            "category",
            "like_count",
            "post_date"
        )


