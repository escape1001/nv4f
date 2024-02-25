from django.db import models

class Spot(models.Model):
    title = models.CharField(max_length=100)
    contents = models.TextField()
    img_path = models.ImageField(upload_to='spot/', blank=True, null=True)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    map_link = models.TextField()
    member = models.CharField(max_length=50, blank=True, null=True)
    source = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title