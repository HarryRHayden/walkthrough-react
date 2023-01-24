from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer


# Create your views here.
class CommentList(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
