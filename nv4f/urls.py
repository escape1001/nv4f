from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from archive import views as archive_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', archive_views.post_list, name='post_list'),
    path('post/', include('archive.urls')),
    path('accounts/', include('accounts.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

''' url 설계
accounts/signup/             # 회원가입
accounts/login/             # 로그인
accounts/logout/             # 로그아웃
accounts/my_info            # 사용자 정보
accounts/my_favorite        # 좋아요 누른 포스트 목록

posts/                       # 전체리스트
posts?cate=123&member=123   # 전체리스트에서 검색
post/<int:pk>/              # 포스트 상세보기
post/create/                # 포스트 작성
post/update/<int:pk>/       # 포스트 수정
post/delete/<int:pk>/       # 포스트 삭제
'''