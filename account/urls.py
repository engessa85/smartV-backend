

from django.urls import path
from .views import GetUserView, login_view, get_user_info

urlpatterns = [
    path('users/',GetUserView.as_view()),
    path('user-login/', login_view),
    path('get-user-info/', get_user_info),
]





