import requests
from allauth.socialaccount.models import SocialAccount
from django.contrib import auth
from django.shortcuts import render

from .models import User, Profile


def login(request):
    return render(request, "login.html")


def profile_register(request):
    code = request.GET['code']
    grant_type = 'authorization_code'
    client_id = 'd01f306c90eda69601dda10cdf62631e'
    redirect_uri = 'http://localhost:8000/profile'
    param = {
        'grant_type': grant_type,
        'client_id': client_id,
        'redirect_uri': redirect_uri,
        'code': code,
    }

    url = 'https://kauth.kakao.com/oauth/token'
    kakao_response = requests.post(url, data=param)
    json_kakao_response = kakao_response.json()

    print(kakao_response.json())
    print("--------------------------------")

    access_token = json_kakao_response['access_token']
    profile_request = requests.post(
        f"https://kapi.kakao.com/v2/user/me",
        headers={"Authorization": f"Bearer {access_token}"},
    )

    profile_json = profile_request.json()
    print(profile_json)

    kakao_account = profile_json.get("kakao_account")

    # 필요한 정보들 알아서 가져오기!
    email = kakao_account.get("email")
    kakao_id = profile_json.get("id")
    profile = kakao_account.get("profile")
    nickname = profile.get("nickname")
    profile_image = profile.get("thumbnail_image_url")
    # data = {'access_token': access_token}
    # accept = requests.post(
    #         f"http://127.0.0.1:8100/account/login/kakao/todjango", data=data
    #     )
    # 정보를 토대로 유저 생성
    user, _ = User.objects.get_or_create(email=email)
    SocialAccount.objects.get_or_create(
        user=user, provider="kakao", uid=kakao_id
    )
    user.save()
    auth.login(request, user)    # 정보를 토대로 프로필 생성
    Profile.objects.get_or_create(user=user, nick=nickname)
    # return redirect("main/")
    return render(request, "profile.html")


