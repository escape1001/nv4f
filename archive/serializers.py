# Post serializers 정의
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    country = serializers.StringRelatedField()
    city = serializers.SlugRelatedField(slug_field='kr_name', read_only=True)
    district = serializers.SlugRelatedField(slug_field='kr_name', read_only=True)
    categories = serializers.StringRelatedField(many=True)
    members = serializers.StringRelatedField(many=True)

    class Meta:
        model = Post
        fields = [
            "id", "country", "city",
            "district", "categories", "members",
            "title", "contents", "thumbnail_image",
            "map_link"
        ]