"""cocialnet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core.views import *
from django.conf import settings # !
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),
    path('posts/<int:id>/', post_detail, name='post-detail'),
    path('post-cbv/<int:id>/', PostDetailView.as_view(), name='post-detail-cbv'),
    path('posts-list-cbv/', PostListView.as_view(), name='posts-list-cbv'),
    path('posts-filter/', PostsFilterView.as_view(), name='posts-filter'),
    path('posts-api/', PostsFromAPI.as_view(), name='posts-api'),
    path('post-detail-api/<int:id>/', PostDetailFromAPI.as_view(), name='post-detail-api'),
    path('posts-api-dos/', PostsFromtoDOS.as_view(), name='posts-api-dos'),
    path('posts-detail-todos/<int:id>/', PostDetailFromtoDOS.as_view(), name='posts-detail-todos'),
    path('profile/<int:id>/', profile_detail, name='profile'),
    path('add-profile/', add_profile, name='add-profile'),
    path('shorts/', shorts, name='shorts-list'),
    path('shorts-cbv/', ShortsListView.as_view(), name='shorts-cbv'),
    path('shorts-filter/', ShortsFilterView.as_view(), name='shorts-filter'),
    path('short/<int:id>/', short_info, name='shorts-info'),
    path('short-cbv/<int:pk>/', ShortDetailView.as_view(), name='short-cbv'),
    path('add-short/', add_short, name='add-short'),
    path('update-short/<int:id>/', update_short, name='update-short'),
    path('saved_posts/', saved_posts_list, name='saved-posts'),
    path('<int:user_id>/', user_posts, name='user-posts'),
    path('add-post/', create_post, name='add-post'),
    path('update-post/<int:id>/', update_post, name='update-post'),
    path('delete-post/<int:id>/', detele_post, name='delete-post'),
    path('add-post-form/', add_post_form, name='add-post-form'),
    path('add-saved/', add_saved, name='add-saved'),
    # path('search/', search, name='search'),
    # path('search-result/', search_result, name='search-result'),
    path('search/', SearchView.as_view(), name='search'),
    path('search-result/', SearchResultView.as_view(), name='search-result'),
    path('subscribes/<int:user_id>/', SubscribesView.as_view(), name='subscribes'),
    path('subscribe/<int:profile_id>/', subscribe, name='subscribe'),
    path('unsubscribe/<int:profile_id>/', unsubscribe, name='unsubscribe'),
    path('notifications/', notifications, name='notifications'),
    path('notifications-cbv/', NotificationView.as_view(), name='notifications-cbv'),
    path('comment-edit/<int:id>/', comment_edit, name='comment-edit'),
    path('comment-delete/<int:id>/', comment_delete, name='comment-delete'),
    path('about/', AboutView.as_view(), name='about'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('faq/', QuestionsView.as_view(), name='faq'),
    path('users/', include('userapp.urls')),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



