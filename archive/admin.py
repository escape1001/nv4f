from django.contrib import admin
from .models import Country, City, District, Post, Category, Member

admin.site.register(Country)
admin.site.register(City)
admin.site.register(District)
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Member)