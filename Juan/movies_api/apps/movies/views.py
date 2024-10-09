from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import MovieSerializer
from .models import Movie


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
 
    filter_backends = [DjangoFilterBackend]  # Add the DjangoFilterBackend
    filterset_fields = {
        "name": ["exact", "icontains"],  # Use a list for multiple lookup types
    }

    # def get_queryset(self):
    #     return Movie.objects.filter(Q(is_private=False) | Q(user=self.request.user))

