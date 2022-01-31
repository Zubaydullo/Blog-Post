from django.db.models import Count
from theblog.models import Post
from rest_framework import generics
from .serializers import PostSerializer


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all().annotate(like_count=Count("likes"))
    serializer_class = PostSerializer


class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all().annotate(like_count=Count("likes"))
    serializer_class = PostSerializer
    lookup_field = "slug"