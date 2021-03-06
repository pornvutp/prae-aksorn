from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'project'

urlpatterns = [
    path('', views.ProjectPage.as_view(), name="home"),
    path("create/", views.ProjectCreate.as_view(), name="create"),
    path("detail/<int:pk>/",views.ProjectDetail.as_view(),name="detail"),
    # path("detail/<int:pk>/create/",views.ItemCreate.as_view(),name="create_item"),

]