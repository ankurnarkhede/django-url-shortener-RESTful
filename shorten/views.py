from django.shortcuts import render

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import url
from .serializers import url_serializer
from django.http import JsonResponse



class url_list(APIView):
    def get(self, request):
        print(self.request.query_params.get('short_hash'), self.request.query_params)
        # shorted = self.request.GET.get('short_hash') # Ek min thamb. mala search karun pahu dekkkk
        shorted = self.request.query_params.get('short_hash')
        try:
            req_url=url.objects.get(short_hash=shorted)
            req_url.count = req_url.count + 1
            req_url.save()
            serializer=url_serializer(req_url)
            return Response(serializer.data)
        except Exception as e:
            print(e)
            return JsonResponse({"mesage": "Requested URL not dfound"})

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



# # def post kam karat ahe ka?...yuppp hoooooooo He run kuthun hotay. Tithe te error print kelay...te get nahi hotey param...me pan try kela hota pahile yane