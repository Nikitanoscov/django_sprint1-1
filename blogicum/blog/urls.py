from django.urls import path

from blog.views import index, category_posts, post_detail

app_name = 'blog'

urlpatterns = [
    path('', index, name='index'),
    path('posts/<int:id>/', post_detail, name='post_detail'),
    path(
        'category/<slug:category_slug>/',
        category_posts,
        name='category_posts'
    )
]
