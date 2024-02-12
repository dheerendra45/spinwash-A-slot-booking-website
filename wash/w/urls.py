from django.urls import path
from .  import views

urlpatterns = [
path('', views.index,name="index"),
path("logout",views.logout_view,name="logout"),
path('book',views.book,name="book"),
path('support',views.support,name="support"),
path('home/',views.home,name="home"),
path('success',views.success,name="success"),

]