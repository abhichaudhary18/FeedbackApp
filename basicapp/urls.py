from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.urls import path,include
from . import views
from django.contrib.auth.decorators import login_required


app_name='basicapp'

urlpatterns = [
path('login/',auth_views.LoginView.as_view(template_name='basicapp/login.html'),name='login'),
path('logout/',login_required(auth_views.LogoutView.as_view()),name='logout'),
path('signup/',views.Signup.as_view(),name='signup'),
path('<username>',views.Sendmess.as_view(),name='send'),
path('inbox/',login_required(views.inbox),name='inbox'),
]
