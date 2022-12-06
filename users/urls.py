from django.urls import path
from users.views import LogoutViews, RegisterViews, LoginViews

urlpatterns = [
    path('login/', LoginViews.as_view()),
    path('logout/', LogoutViews.as_view()),
    path('register/', RegisterViews.as_view())
]