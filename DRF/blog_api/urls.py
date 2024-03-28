from django.urls import path
from blog_api.views import PostList , PostDetail
app_name = "blog_api"
urlpatterns = [
    path('',PostList.as_view() ,name ="listcreate"),
    path('<int:pk>/',PostDetail.as_view() , name ="detailcreate")
]