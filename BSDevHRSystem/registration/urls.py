from django.urls import path
from .views import views
from .views.change_password_views import ChangePasswordView
app_name = 'accounts'

urlpatterns = [
    #path('',views.index,name='index'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('change_password/',ChangePasswordView.as_view(),name='change_password'),
]