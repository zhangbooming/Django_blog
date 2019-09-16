from django.urls import path, include
import blog.views
urlpatterns = [
    path('hello_world', blog.views.hello_world),
    path('boyang', blog.views.boyang),
    path('content', blog.views.artical_content),
    path('index', blog.views.get_index_page),
    path('test', blog.views.test),
    path('detail/<int:artical_id>', blog.views.get_detail_page),
]