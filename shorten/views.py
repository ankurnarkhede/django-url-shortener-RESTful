from django.shortcuts import render

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import url
from .serializers import url_serializer


from .models import url
from rest_framework import viewsets
from .serializers import url_serializer



class url_list(APIView):

    def get(self, request):
        # urls=url.objects.get(short_hash="qwertyui")
        urls = url.objects.all()
        serializer=url_serializer(urls, many=True)
        return Response(serializer.data)

    def post(self, request):
        long_url = request.POST.get('long_url', None)
        short_hash = request.POST.get('short_hash', None)
        count = 0

        url (
            long_url=long_url,
            short_hash=short_hash,
            count=count,
        ).save()

        urls = url.objects.all ()
        serializer = url_serializer (urls, many=True)
        return Response (serializer.data)


