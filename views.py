from cgitb import html
from html.entities import html5
from core.api.erasebg import EraseBackground
from core.models import EraseBackgroundModel
from core.serializers import EraseBackgroundSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status




class EraseBackgroundView (APIView):
    name = 'Remove background'

    def get(self, request):
        eraseBackground = EraseBackgroundModel.objects.all()
        serializer = EraseBackgroundSerializer(eraseBackground, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request):
       # template_name = 'image'
        file_obj = request.data
        print(file_obj )
       # file = EraseBackground().removeBg(file_obj=file_obj)

        #serializer = EraseBackgroundSerializer()
        #serializer.is_valid(raise_exception=True)
        #serializer.save()
        # EraseBackground().removeBacground(
        #   inputPath='/media/roger/Dados/Pycharm-Projects/imageupload/media/d68f6314-5daf-4307-857d-7fdebab67db0-backgroundremoved362f67ca-6f4b-4f83-94d9-ebfbc8cd049b.jpeg',
        #  outputPath='/media/roger/Dados/Pycharm-Projects/imageupload/media/d68f6314-5daf-4307-857d-7fdebab67db0-backgroundremoved362f67ca-6f4b-4f83-94d9-ebfbc8cd049b'+'removed'+'.jpeg')
        # print('resutado', request.data)

        return Response({"target" : "foi"})
