from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from genres.models import Genre
from app.permissions import GlobalDefaultPermissions
from genres.serializers import GenreSerializer
#from genres.permissions import GenrePermisssionClass

class GenreCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    
