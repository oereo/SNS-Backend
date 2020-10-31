from django.shortcuts import render, redirect
import requests
from .models import User, Profile
from allauth.socialaccount.models import SocialAccount


def login(request):
    return render(request, "login.html")


# def kakao_callback(request):
#     app_rest_api_key = 'd01f306c90eda69601dda10cdf62631e'
#     redirect_uri = "http://localhost:8000/oauth"
#     user_token = request.GET.get("code")
#
#
#     token_request = requests.post(
#         f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={app_rest_api_key}&redirect_uri={redirect_uri}&code={user_token}"
#     )
#
#     token_response_json = token_request.json()
#     print(token_response_json)
#     access_token = token_response_json.get("access_token")
#     print(access_token)
#
#     profile_request = requests.post(
#         f"https://kapi.kakao.com/v2/user/me",
#         headers={"Authorization": f"Bearer {access_token}"},
#     )
#     profile_json = profile_request.json()
#     print(profile_json)
#     kakao_account = profile_json.get("kakao_account")
#     email = kakao_account.get("email", None)
#     profile = kakao_account.get("profile")
#     nickname = profile.get("nickname")
#     profile_image = profile.get("thumbnail_image_url")
#
#     user, _ = User.objects.get_or_create(email=email)
#     SocialAccount.objects.get_or_create(
#         user=user, provider="kakao", uid=user.id
#     )
#     return redirect("profile_register")


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
    r = requests.post(url, data=param)
    json_result = r.json()
    print(r.json())
    print("--------------------------------")
    access_token = json_result['access_token']
    profile_request = requests.post(
        f"https://kapi.kakao.com/v2/user/me",
        headers={"Authorization": f"Bearer {access_token}"},
    )
    profile_json = profile_request.json()
    print(profile_json)
    kakao_account = profile_json.get("kakao_account")
    email = kakao_account.get("email")
    kakao_id = profile_json.get("id")
    profile = kakao_account.get("profile")
    nickname = profile.get("nickname")
    profile_image = profile.get("thumbnail_image_url")
    print(kakao_id)
    user, _ = User.objects.get_or_create(email=email)
    SocialAccount.objects.get_or_create(
        user=user, provider="kakao", uid=kakao_id
    )
    Profile.objects.get_or_create(user=user, nick=nickname)

    return render(request, "profile.html", {'access_token': access_token})
