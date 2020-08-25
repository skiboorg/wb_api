from rest_framework.pagination import PageNumberPagination

from .serializers import *
from rest_framework.views import APIView
from .models import *
from rest_framework.response import Response
from rest_framework import generics


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 1000
    page_size_query_param = 'page_size'
    max_page_size = 10000

class PostsResultsSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 10000

    def get_paginated_response(self, data):
        return Response({
            'links':{
                'next': self.get_next_link(),
                'prev': self.get_previous_link(),
            },
            'page_count':self.page.paginator.count,
            'results':data
        })


class GetPosts(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PostsResultsSetPagination

class GetPost(generics.RetrieveAPIView):
    queryset = Post.objects.filter()
    lookup_field = 'name_slug'
    serializer_class = PostSerializer


class BlackListItems(generics.ListAPIView):
    queryset = BlackListItem.objects.all()
    serializer_class = BlItemSerializer
    pagination_class = LargeResultsSetPagination


class GetPostsByTag(generics.ListAPIView):
    serializer_class = PostSerializer
    pagination_class = PostsResultsSetPagination
    def get_queryset(self):
        tag_id=self.request.query_params.get('tag')
        if tag_id != '0':
            posts = Post.objects.filter(tags__in=[tag_id])
        else:
            posts = Post.objects.all()
        return posts



class GetTags(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    pagination_class = LargeResultsSetPagination
