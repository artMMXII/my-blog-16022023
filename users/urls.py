from django.urls import path
from users.views import RegisterView, LoginUser, logout_user, profile


urlpatterns = [
    path('registration/', RegisterView.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('profile/', profile, name='profile'),
    path('logout/', logout_user, name='logout'),
]
