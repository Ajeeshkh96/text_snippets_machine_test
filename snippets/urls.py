from django.urls import path
from .views import UserLoginView, UserRegisterView, CreateSnippetAPIView, SnippetDetailAPIView, SnippetUpdateAPIView, SnippetDeleteAPIView, TagListAPIView, TagDetailAPIView, OverviewAPIView, SnippetListAPIView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('snippets/create/', CreateSnippetAPIView.as_view(), name='create_snippet'),
    path('snippets/<int:pk>/', SnippetDetailAPIView.as_view(), name='snippet-detail'),
    path('snippets/<int:pk>/update/', SnippetUpdateAPIView.as_view(), name='snippet-update'),
    path('snippets/<int:pk>/delete/', SnippetDeleteAPIView.as_view(), name='snippet-delete'),
    path('tags/', TagListAPIView.as_view(), name='tag-list'),
    path('tags/<int:pk>/', TagDetailAPIView.as_view(), name='tag-detail'),
    path('overview/', OverviewAPIView.as_view(), name='overview'),
    path('snippets/', SnippetListAPIView.as_view(), name='snippet-list'),
]
