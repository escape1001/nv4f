from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from archive.serializers import PostSerializer
from .models import Post


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
    pass

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def post_like_toggle(request):
    pass

