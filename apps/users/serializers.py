from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import OwnerProfile, TenantProfile

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "phone",
            "role",
            "created_at",
        ]
        read_only_fields = [
            "id",
            "role",
            "created_at",
        ]


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        min_length=8
    )
    password_confirmation = serializers.CharField(
        write_only=True
    )

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password",
            "password_confirmation",
            "first_name",
            "last_name",
            "phone",
            "role",
        ]

    def validate(self, attrs):
        if attrs["password"] != attrs["password_confirmation"]:
            raise serializers.ValidationError({
                "password_confirmation": "Les mots de passe ne correspondent pas."
            })

        if attrs["role"] == User.Role.ADMIN:
            raise serializers.ValidationError({
                "role": "La création d'un administrateur est interdite."
            })

        return attrs

    def create(self, validated_data):
        validated_data.pop("password_confirmation")

        password = validated_data.pop("password")

        user = User(**validated_data)
        user.set_password(password)
        user.save()

        if user.role == User.Role.OWNER:
            OwnerProfile.objects.create(user=user)

        elif user.role == User.Role.TENANT:
            TenantProfile.objects.create(user=user)

        return user


class OwnerProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = OwnerProfile
        fields = [
            "id",
            "user",
            "national_id",
            "address",
            "verification_status",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "user",
            "verification_status",
            "created_at",
            "updated_at",
        ]


class TenantProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = TenantProfile
        fields = [
            "id",
            "user",
            "national_id",
            "address",
            "verification_status",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "user",
            "verification_status",
            "created_at",
            "updated_at",
        ]
        
class UserUpdateSerializer(serializers.ModelSerializer):
    
    class Mete:
        model=User
        
        fields=[
            "first_name",
            "last_name",
            "email",
            "phone",
        ]
    def validate(self,value):
        user=self.instance
        
        if user.objects.filter(email=value).exclude(pk=user.pk).exists():
            raise serializers.ValidationError("cette adresse email est deja utilisee")
        return value
    
class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(
        write_only=True
    )

    new_password = serializers.CharField(
        write_only=True,
        min_length=8
    )

    new_password_confirmation = serializers.CharField(
        write_only=True
    )

    def validate_old_password(self, value):
        user = self.context["request"].user

        if not user.check_password(value):
            raise serializers.ValidationError(
                "L'ancien mot de passe est incorrect."
            )

        return value

    def validate(self, attrs):
        if (
            attrs["new_password"]
            != attrs["new_password_confirmation"]
        ):
            raise serializers.ValidationError({
                "new_password_confirmation":
                    "Les mots de passe ne correspondent pas."
            })

        return attrs