from .import views
from django.urls import path

app_name = "polls"
urlpatterns = [
    path("",views.index,name="index"),
    
    path("", views.index, name="index"),
    
    path("<int:question_id>/", views.detail, name="detail"),
    
    path("<int:question_id>/results/", views.result, name="results"),
    
    path("<int:question_id>/vote/", views.vote, name="vote"),
    
] 