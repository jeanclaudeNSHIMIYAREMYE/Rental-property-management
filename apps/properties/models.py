from django.conf import settings
from django.db import models
from django.core.validators import MinValueValidator

class Property(models.Model):

    class PropertyType(models.TextChoices):
        HOUSE = "HOUSE", "Maison"
        APARTMENT = "APARTMENT", "Appartement"
        VILLA = "VILLA", "Villa"
        STUDIO = "STUDIO", "Studio"
        OFFICE = "OFFICE", "Bureau"
        COMMERCIAL = "COMMERCIAL", "Commercial"

    class Status(models.TextChoices):
        AVAILABLE = "AVAILABLE", "Disponible"
        RESERVED = "RESERVED", "Réservé"
        OCCUPIED = "OCCUPIED", "Occupé"
        MAINTENANCE = "MAINTENANCE", "Maintenance"
        UNAVAILABLE = "UNAVAILABLE", "Indisponible"

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="properties",
    )

    title = models.CharField(max_length=200)

    description = models.TextField()

    property_type = models.CharField(
        max_length=20,
        choices=PropertyType.choices,
    )

    address = models.CharField(max_length=255)

    neighborhood = models.CharField(
        max_length=150,
        blank=True,
    )

    city = models.CharField(max_length=100)

    bedrooms = models.PositiveIntegerField(default=0,validators=[MinValueValidator])

    bathrooms = models.PositiveIntegerField(default=0,validators=[MinValueValidator])

    surface_area = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator],
    )

    monthly_rent = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        validators=[MinValueValidator],
    )

    deposit = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
        validators=[MinValueValidator],
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.AVAILABLE,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
    
    
class PropertyImage(models.Model):
     property=models.ForeignKey(Property,on_delete=models.CASCADE,related_name="images")
     image=models.ImageField(upload_to="properties/")
     caption=models.CharField(max_length=255,blank=True)
     created_at=models.DateTimeField(auto_now_add=True)
     
     class Meta:
         ordering=["created_at"]
     def __str__(self):
         return f"Image-{self.property.title}"
         
    
    
    
        
