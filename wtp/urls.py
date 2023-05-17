from django.urls import path
from . import views

urlpatterns = [
    # path('<int:pk>/', views.wtp_detail),
    path('', views.wtp_list),
    # path('depression', views.Depression.as_view()),
    path('gender', views.Gender.as_view()),
    path('age', views.Age.as_view()),
    # path('fine', views.Fine.as_view()),
    # path('good', views.Good.as_view()),


]