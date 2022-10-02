from django.shortcuts import render, redirect
from .models import UserModel
from django.http import HttpResponse
from django.contrib.auth import get_user_model #사용자가 있는지 검사하는 함수
from django.contrib import auth # 사용자 auth 기능

def sign_up_view(request):
    if request.method == 'GET':
        return render(request, 'user/signup.html')
    elif request.method == 'POST':
        email = request.POST.get('email', None)
        username = request.POST.get('username', None)
        nickname = request.POST.get('nickname', None)
        password = request.POST.get('password', None)
        password2 = request.POST.get('password2', None)
        
        if password != password2:
            return render(request, 'user/signup.html')
        else:
            exist_email = get_user_model().objects.filter(email=email)
            if exist_email:
                return render(request, 'user/signup.html')
            else:
                UserModel.objects.create_user(email=email, username=username, password=password, nickname=nickname)
                return redirect('/sign-in') # 회원가입이 완료되었으므로 로그인 페이지로 이동
    

# user/views.py
def sign_in_view(request):
    if request.method == 'POST':
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)

        me = auth.authenticate(request, email=email, password=password) # 사용자 불러오기
        if me is not None:  # 저장된 사용자의 패스워드와 입력받은 패스워드 비교
            auth.login(request, me)
            return redirect('/')
        else: # 로그인이 실패하면 다시 로그인 페이지를 보여주기
            return redirect('/sign-in')
    elif request.method == 'GET':
        return render(request, 'user/signin.html')