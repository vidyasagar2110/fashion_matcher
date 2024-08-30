from django.db import models

class ClothingItem(models.Model):
    url = models.URLField(max_length=200)
    category = models.CharField(max_length=50)  # e.g., 'shirt', 'pants'
    created_at = models.DateTimeField(auto_now_add=True)
