from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status,generics, permissions, mixins
from django.conf import settings
from django.contrib import auth
import jwt
import requests
from movies.settings import Username, Password
import json
from django.http import HttpResponse, JsonResponse
from movie.serializers import RegisterSerializer, UserSerializer
from movie.models import *
from django.views.generic.detail import DetailView
from django.views.decorators.csrf import csrf_exempt


class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user,    context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        })



def movie(request):
    print('####')
    url = 'https://demo.credy.in/api/v1/maya/movies/'
    auth = (Username,Password)
    re = requests.get(url,auth=auth)
    response = re.json()
    print(re.text)
    data = response['results']
    collection = []
    for i in data:
        title = i['title']
        print(title)
        description = i['description']
        uuid = i['uuid']
        data = {'title':title,'description':description,'uuid':uuid}
        collection.append(data)

    print(collection)
    return JsonResponse(response)


@csrf_exempt
def collection(request):
    if request.method =='GET':
        response = {"is_success" : True, "response_message" : "" , \
                "data":{},"response_code" : 200}
        url = 'https://demo.credy.in/api/v1/maya/movies/'
        auth = (Username,Password)
        re = requests.get(url,auth=auth)
        print(re)
        respon = re.json()
        print(respon)
        # print(respon['results'])
        # print(re.text)
        # data = response['results']
        data = respon['results']
        collection = []
        for i in data:
            title = i['title']
            print(title)
            description = i['description']
            uuid = i['uuid']
            data = {'title':title,'description':description,'uuid':uuid}
            collection.append(data)
        response['data'] = collection
        print(response)
        # resp = json.dumps(response)
        return JsonResponse(response)
    if request.method == 'POST':
        response = {"is_success" : True, "response_message" : "" , \
                "data":{},"response_code" : 200}
        print('#####')
        print(request.body)

        res = json.loads(request.body)
        print(res)

        title = res.get('title')
        description = res.get('description')
        movies = res.get('movies')
        uuid = []
        print(title,description,movies)
        for i in movies:
            data = Collection.objects.create(title=title,description=description,movie_titel=i['title'],\
                    movie_description=i['description'],movie_genres=i['genres'],uuid=i['uuid'])
            # print(data)
            data.save();
            uuid.append(i['uuid'])
        response['response_message'] = 'Data dsave in database'
        response['data'] = uuid

        return JsonResponse(response)



class Collectionview(DetailView):
    print("$$$")
    model = Collection
    print('mrefim')

    def get_context_data(self, **kwargs):
        print("EEEE",super().get_context_data(**kwargs))
        return Collection.objects.get(movie_uuid=self.kwargs.get("uuid"))

        



