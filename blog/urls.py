from django.urls import path, include
from . import views

# 전체 서비스에 지금 이 앱을 blog라고 부르기로 약속하는 것
app_name = "blog"
# 각 앱에 이름이 겹치는 파일 혹은, url이 겹치는 주소가 있을 수 있습니다.
# 그때 app_name : name 순으로 url을 호출해주시면
# 겹치는 파일명에도 불구하고 별개의 자리를 절대경로화해서 접근할 수 있습니다.

# blog 앱 내부 경로를 지정하는 부분
urlpatterns = [
    path('', views.BlogHome.as_view(paginate_by=5), name="home"),
    # paginate_by=개수
    path('post_list/', views.PostList.as_view(), name="post_list"), # '' : blog 뒤에 달린 주소가 없음을 의미함 
    path('<int:pk>/', views.PostDetail.as_view()),
    path('about/', views.about_me, name="about_me"), # name="별명" // Alias
    path('contact/', views.contact, name="contact"),  
    # "blog" 라는 app의 "contact" 라는 별명으로 주소/blog/contact/를 호출할 수 있게 됩니다
    path('category/<str:slug>/', views.category_posts),
    # path('index2/', views.index2)  # 주소/blog/index2
    path('create_post/', views.PostCreate.as_view()),
]

