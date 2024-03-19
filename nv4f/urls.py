from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('spot.urls')),
    path('user/', include('user.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

''' url 설계
accounts/signup/             # 회원가입
accounts/login/             # 로그인
accounts/logout/             # 로그아웃
accounts/myinfo             # 사용자 정보
accounts/my_favorite        # 좋아요 누른 포스트 목록

posts/                       # 전체리스트
posts?cate=123&member=123   # 전체리스트에서 검색
post/<int:pk>/              # 포스트 상세보기
post/create/                # 포스트 작성
post/update/                # 포스트 수정
post/delete/                # 포스트 삭제
'''