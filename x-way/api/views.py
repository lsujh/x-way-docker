from django.contrib.auth import get_user_model, login
from django.contrib.auth.hashers import check_password

from rest_framework.generics import ListAPIView, RetrieveDestroyAPIView, UpdateAPIView
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework_simplejwt.views import TokenObtainPairView

from placeholder.models import Album
from .serializers import AlbumSerializer, PhotosAlbumSerializer, RegistrationSerializer

User = get_user_model()


class RegistrationAPIView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

    def perform_create(self, serializer):
        return serializer.save()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserTokenObtainPairView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer

    def post(self, request, *args):
        email = request.data.get("email")
        password = request.data.get("password")
        login_serializer = TokenObtainPairSerializer(data=request.data)
        user = User.objects.filter(email=email).first()
        if not user:
            return Response({"detail": "Wrong credentials"}, status=400)
        if not check_password(password, user.password):
            return Response({"detail": "Wrong credentials"}, status=400)
        if login_serializer.is_valid():
            login(request, user=user)
            refresh = RefreshToken.for_user(user=user)
            return Response(
                {
                    "token": {
                        "access": str(refresh.access_token),
                        "refresh": str(refresh),
                    },
                },
                status=200,
            )
        else:
            return Response(login_serializer.errors, status=400)


class AlbumsApi(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()


class PhotosAlbumApi(RetrieveDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PhotosAlbumSerializer
    queryset = Album.objects.all()


class AlbumUpdateApi(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()
