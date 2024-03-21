from django.db import models
from django.contrib.auth.models import User

    
class Country(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.country} > {self.name}"

class District(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.city} > {self.name}"
    
class Post(models.Model):
    LEVEL_CHOICES = [
        (1, 'LV1'),  # 기본
        (2, 'LV2'),  # 편집자
        (3, 'LV3'),  # 관리자
    ]

    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    is_show = models.BooleanField(default=True)
    level = models.IntegerField(choices=LEVEL_CHOICES, default=1)
    contents = models.TextField()
    thumbnail_image = models.ImageField(upload_to='post/thumbnails/%Y/%m/%d/', blank=True, null=True)
    map_link = models.TextField(blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True, blank=True)
    categories = models.ManyToManyField('Category', blank=True)
    members = models.ManyToManyField('Member', blank=True)

    def __str__(self):
        return self.title
    

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name
    

class Member(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name
    

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} > {self.post.title}"