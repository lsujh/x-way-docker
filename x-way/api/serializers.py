from django.contrib.auth import get_user_model
from django.contrib.auth import password_validation as validators

from rest_framework import serializers, exceptions

from placeholder.models import Album, Photo

User = get_user_model()


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "email",
            "password",
        )
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, data):
        user = User(**data)
        password = data.get("password")
        errors = dict()
        try:
            validators.validate_password(password=password, user=user)
        except exceptions.ValidationError as e:
            errors["password"] = list(e.messages)
        if errors:
            raise serializers.ValidationError(errors)
        return super(RegistrationSerializer, self).validate(data)

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = (
            "id",
            "userId",
            "title",
        )
        read_only = ("id",)


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = (
            "id",
            "albumId",
            "title",
            "url",
            "thumbnailUrl",
            "photo",
        )


class PhotosAlbumSerializer(serializers.ModelSerializer):
    photo = PhotoSerializer(source="photo_set", many=True)

    class Meta:
        model = Album
        fields = (
            "id",
            "userId",
            "title",
            "photo",
        )
