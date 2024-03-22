from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from archive.serializers import PostSerializer
from .models import Post, Country, Category, Member, Like
from django.shortcuts import get_object_or_404


@api_view(["GET"])
def post_list(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)

    return Response(serializer.data)

@api_view(["GET", "PUT", "DELETE"])
def post_detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except :
        return Response({"error": "존재하지 않는 게시글입니다."}, status=404)
    
    if request.method == "GET":
        serializer = PostSerializer(post)

        return Response(serializer.data)
    
    elif request.method == "PUT":
        if not request.user.is_authenticated:
            return Response({"error": "로그인이 필요합니다."}, status=401)
        if request.user != post.author:
            return Response({"error": "작성자만 수정할 수 있습니다."}, status=403)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
        
    elif request.method == "DELETE":
        if not request.user.is_authenticated:
            return Response({"error": "로그인이 필요합니다."}, status=401)
        if request.user != post.author:
            return Response({"error": "작성자만 삭제할 수 있습니다."}, status=403)
        post.delete()
        return Response(status=204)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def post_create(request):
    serialrizer = PostSerializer(data=request.data)
    if serialrizer.is_valid():
        serialrizer.save(author=request.user)
        return Response(serialrizer.data, status=201)
    
    return Response(serialrizer.errors, status=400)

@api_view(["GET"])
def post_filter_list(request):
    categories = request.GET.getlist("categories")
    members = request.GET.getlist("members")
    country = request.GET.get("country")
    city = request.GET.get("city")
    district = request.GET.get("district")

    '''아래 모양으로 리턴
    {
        categories : ['음식', '숙소'],
        members : ['홍길동', '김철수'],
        locations : [
            {
                country_name : '한국',
                city : [
                    {
                        city_name : '서울',
                        district : ['강남', '강북']
                    }
                ]
            },
            {
                country_name : '일본',
                city : [
                    {
                        city_name : '도쿄',
                        district : ['신주쿠', '아키하바라']
                    }
                ]
            }
        ]
    }
    '''

    locations = []

    for country in Country.objects.all():
        country_data = {
            "country_name": country.name,
            "city": []
        }
        for city in country.city_set.all():
            city_data = {
                "city_name": city.name,
                "district": city.district_set.values_list("name", flat=True)
            }
            country_data["city"].append(city_data)
        locations.append(country_data)

    data = {
        "categories": Category.objects.filter(name__in=categories).values_list("name", flat=True),
        "members": Member.objects.filter(name__in=members).values_list("name", flat=True),
        "locations": locations
    }

    return Response(data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def post_like_toggle(request, pk):
    post = get_object_or_404(Post, pk=pk)
    user = request.user
    liked_post_ids = user.likes.values_list('post__id', flat=True)

    if post.id in liked_post_ids:
        like = Like.objects.get(user=user, post=post)
        like.delete()
        return Response(status=204)
    else:
        like = Like.objects.create(user=user, post=post)
        like.save()
        return Response(status=201)
