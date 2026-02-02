from django.urls import path

from . import views

from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('signup/',
         views.SignUpView.as_view(),
         name = 'signup'),
    
    path('signup_success/',
         views.SignUpSuccessView.as_view(),
         name='signup_success'),

    path('login/',
         auth_views.LoginView.as_view(template_name='login.html'),
         name='login'
        ),

    path('logout/',
         auth_views.LogoutView.as_view(template_name='logout.html'),
         name='logout'
        ),
   
    path('mypage/',
          views.MyPageView.as_view(),
          name="mypages"
          ),

    path('mypage/edit/',
          views.ActivProfileUpdateView.as_view(),
          name="profile_edit"
          ),

    path('mypage/create/',
         views.ProfileCreateView.as_view(),
         name='profile_create'),
   
    path('profile/select/<int:profile_id>/',
         views.SelectProfileView.as_view(),
         name='profile_select'),

    
]
