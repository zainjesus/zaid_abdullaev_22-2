from django.urls import path
from users.views import LogoutViews, RegisterView, LoginView

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('logout/', LogoutViews.as_view()),
    path('register/', RegisterView.as_view())
]