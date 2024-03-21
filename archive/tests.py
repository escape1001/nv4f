from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Post

class AccountsTest(TestCase):
    def setUp(self):
        self.client = Client()

        self.user = User.objects.create_user(username='test', password='test1234!')
        self.user.save()

        self.user2 = User.objects.create_user(username='test2', password='test1234!')
        self.user2.save()

        self.post_001 = Post.objects.create(
            title='첫 번째 포스트입니다.',
            content='Hello, World. We are the world.',
            user=self.user
        )
        self.post_001.save()

        
    # 포스트 좋아요 토글 테스트
    def test_post_like(self):
        print('포스트 좋아요 토글 테스트')
        print('>> 비회원 좋아요 불가')
        response = self.client.post(f'/archive/post/like/1')
        self.assertEqual(response.status_code, 401)

        self.client.login(username='test', password='test1234!')
        print('>> 회원 좋아요 토글')
        response = self.client.post(f'/archive/post/like/1')
        self.assertEqual(response.status_code, 201)
        print(f'>> 좋아요 클릭1 메세지 : {response.data}')

        response = self.client.post(f'/archive/post/like/1')
        self.assertEqual(response.status_code, 204)
        print(f'>> 좋아요 클릭2 메세지 : {response.data}')

        
    # 비회원 포스트 CUD 테스트
    def test_post_cud_nomember(self):
        print('비회원 포스트 CUD 테스트')
        print('>> 비회원 포스트 생성 시도')
        response = self.client.post('/archive/post/',{
                'title' : '생성테스트',
                'contents' : '설명글~~',
                'author' : self.user.id,
                'country' : '대한민국',
            },
            format='json'
        )
        self.assertEqual(response.status_code, 401)
        
        print('>> 비회원 포스트 수정 시도')
        response = self.client.put('/archive/post/1',{
                'title' : '수정테스트',
                'contents' : '설명글~~',
                'author' : self.user.id,
                'country' : '대한민국',
            },
            format='json'
        )
        self.assertEqual(response.status_code, 401)
        
        print('>> 비회원 포스트 삭제 시도')
        response = self.client.delete('/archive/post/1')
        self.assertEqual(response.status_code, 401)

        
    # 회원 포스트 CUD 테스트
    def test_post_cud_nomember(self):
        print('회원 포스트 CUD 테스트')
        print('>> 회원 포스트 생성 시도')
        self.client.login(username='test', password='test1234!')
        response = self.client.post('/archive/post/',{
                'title' : '생성테스트',
                'contents' : '설명글~~',
                'author' : self.user.id,
                'country' : '대한민국',
            },
            format='json'
        )
        post_id = response.data['id']
        print(f'>> 생성된 포스트 data : {response.data}')
        self.assertEqual(response.status_code, 201)
        
        print('>> 회원타인 포스트 수정 시도')
        self.client.logout()
        self.user = User.objects.create_user(username='test2', password='test1234!')
        response = self.client.put(f'/archive/post/{post_id}',{
                'title' : '수정테스트',
                'contents' : '설명글~~',
                'author' : self.user.id,
                'country' : '대한민국',
            },
            format='json'
        )
        self.assertEqual(response.status_code, 403)
        
        print('>> 회원타인 포스트 삭제 시도')
        response = self.client.delete(f'/archive/post/{post_id}')
        self.assertEqual(response.status_code, 403)
        
        print('>> 회원본인 포스트 수정 시도')
        self.client.logout()
        self.user = User.objects.create_user(username='test', password='test1234!')
        response = self.client.put(f'/archive/post/{post_id}',{
                'title' : '수정테스트',
                'contents' : '설명글~~',
                'author' : self.user.id,
                'country' : '대한민국',
            },
            format='json'
        )
        print(f'>> 수정된 포스트 data : {response.data}')
        self.assertEqual(response.status_code, 200)
        
        print('>> 회원타인 포스트 삭제 시도')
        response = self.client.delete(f'/archive/post/{post_id}')
        self.assertEqual(response.status_code, 204)