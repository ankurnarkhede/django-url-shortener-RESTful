from django.shortcuts import render

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import url
from .serializers import url_serializer


class url_list(APIView):

    def get(self, request):
        # urls=url.objects.get(short_hash=lol)
        urls = url.objects.all()
        serializer=url_serializer(urls, many=True)
        return Response(serializer.data)

    def post(self):
        pass

