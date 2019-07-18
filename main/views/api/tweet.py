import django_filters
from rest_framework import viewsets, filters

from main.models import Tweet
from main.serializers import TweetSerializer

class TweetViewSet(viewsets.ModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer


# from rest_framework.response import Response
# from rest_framework.generics import GenericAPIView
# from rest_framework.mixins import RetrieveModelMixin
# from rest_framework.viewsets import GenericViewSet
# from rest_framework.decorators import schema
# from rest_framework.schemas import ManualSchema


# class TweetView(GenericAPIView):
#     serializer_class = TweetSerializer

    # @schema(ManualSchema(fields=[]))
    # def get(self, request):
    #     serializer = UserSerializer(request.user)
    #     return Response(serializer.data)

    # def put(self, request):
    #     serializer = UserSerializer(request.user, data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)


# class TweetViewSet(RetrieveModelMixin, GenericViewSet):
#     serializer_class = UserSerializer
#     queryset = User.objects.all()
