from django.urls import path
# from . import views
from .views import LikeView, HomeView, \
    ArticleDetailView, AddPostView, \
    UpdatePostView, DeletePostView, AddCategoryView, categories, category_list


urlpatterns = [
    # path('', views.home, name='home'),
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article_detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('category/<str:cats>/', categories, name="category"),
    path('category-list/', category_list, name="category-list"),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('update_post/<int:pk>/', UpdatePostView.as_view(), name="update_post"),
    path('delete_post/<int:pk>/', DeletePostView.as_view(), name="delete_post"),
    path('like/<int:pk>/', LikeView, name='like_post'),
]
