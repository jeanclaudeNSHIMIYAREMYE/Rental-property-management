from django.contrib.auth import get_user_model
from django.db import transaction
from .models import  OwnerProfile,TenantProfile


User=get_user_model


@transaction.atomic
def register_user(
    *,
    username,
    email,
    password,
    role,
    first_name="",
    last_name="",
    phone=None,
):
    user=User.objects.create_user(
        username=username,
        email=email,
        password=password,
        role=role,
        first_name=first_name,
        last_name=last_name,
        phone=phone
    )
    if role==User.Role.OWNER:
        OwnerProfile.objects.create(user=user)
    if role==User.Role.TENANT:
        TenantProfile.objects.create(user=user)

    return user   
    