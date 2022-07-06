from django.urls import path, include

from accounts.views import RegisterFormView, LoginFormView, LogoutFormView

urlpatterns = [
    path('', RegisterFormView.as_view(), name='register'),
    path('login/', LoginFormView.as_view(), name='login'),
    path('logout/', LogoutFormView.as_view(), name='logout'),
    path('login/bookstore/', include('bookstore.urls'), name='bookstore')
]
