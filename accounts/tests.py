from django.test import TestCase, Client
from .models import CustomUser

class AccountsTest(TestCase):
    def setUp(self):
        self.client = Client()

        self.user = CustomUser.objects.create_user(username='test', password='test1234!')
        self.user.save()

        
    # 로그인 권한 있어야만 접근할 수 있는 url 테스트
    def test_login_required(self):
        print('로그인 권한 있어야만 접근할 수 있는 url 테스트')
        print('>> 비회원 my_info 접근 시도')
        response = self.client.get('/accounts/my_info/')
        self.assertEqual(response.status_code, 401)
        
        print('>> 비회원 my_favorite 접근 시도')
        response = self.client.get('/accounts/my_favorite/')
        self.assertEqual(response.status_code, 401)


        print('>> 회원 my_info 접근 시도')
        self.client.login(username='test', password='test1234!')
        response = self.client.get('/accounts/my_info/')
        self.assertEqual(response.status_code, 200)
        print(f'>> 회원 my_info : {response}')

        print('>> 회원 my_favorite 접근 시도')
        response = self.client.get('/accounts/my_favorite/')
        self.assertEqual(response.status_code, 200)
        print(f'>> 회원 my_favorite : {response}')