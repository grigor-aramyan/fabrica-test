from django.urls import path
from survey import views

urlpatterns = [
    path('surveys/list', views.survey_list),
    path('surveys/result/<int:user_id>/', views.survey_result),
]