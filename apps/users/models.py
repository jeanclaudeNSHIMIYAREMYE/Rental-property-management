from email.policy import default

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    
    class Role(models.TextChoices):
        ADMIN="ADMIN", "Administrateur",
        OWNER="OWNER", "Propriétaire",
        TENANT="TENANT", "Locataire",
    
    email = models.EmailField(unique=True)
    first_name=models.CharField(max_length=30, blank=True, null=True)
    last_name=models.CharField(max_length=30, blank=True, null=True)
    phone=models.CharField(max_length=20, blank=True, null=True,unique=True)
    role=models.CharField(max_length=20, choices=Role.choices, default=Role.TENANT)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.email
class OwnerProfile(models.Model):
    
    class VerificationStatus(models.TextChoices):
        PENDING="PENDING", "En attente",
        VERIFIED="VERIFIED", "Vérifié",
        REJECTED="REJECTED", "Rejeté",
    user=models.OneToOneField(User, on_delete=models.CASCADE, related_name='owner_profile')
    national_id=models.CharField(max_length=100, blank=True, null=True)
    address=models.CharField(max_length=255, blank=True, null=True)
    verification_status=models.CharField(max_length=20, choices=VerificationStatus.choices, default=VerificationStatus.PENDING)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"OwnerProfile for {self.user}"
    
class TenantProfile(models.Model):
        class VerificationStatus(models.TextChoices):
            PENDING="PENDING", "En attente",
            VERIFIED="VERIFIED", "Vérifié",
            REJECTED="REJECTED", "Rejeté",
        user=models.OneToOneField(User, on_delete=models.CASCADE, related_name='tenant_profile')
        national_id=models.CharField(max_length=100, blank=True, null=True)
        address=models.CharField(max_length=255, blank=True, null=True)
        verification_status=models.CharField(max_length=20, choices=VerificationStatus.choices, default=VerificationStatus.PENDING)
        created_at=models.DateTimeField(auto_now_add=True)
        updated_at=models.DateTimeField(auto_now=True)

        def __str__(self):
            return f"TenantProfile for {self.user}"