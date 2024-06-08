from django.urls import path
from .views import IndexView, SessionCreateView, SessionGetView, SessionUpdateView, ScreenshotCreateView

urlpatterns = [
  path('', IndexView.as_view(), name='index'),
  path('api/session/create/', SessionCreateView.as_view(), name='session-create'),
  path('api/session/get/<int:pk>/', SessionGetView.as_view(), name='session-get'),
  path('api/session/update/<int:pk>/', SessionUpdateView.as_view(), name='session-update'),
  path('api/screenshot/create/', ScreenshotCreateView.as_view(), name='screenshot-create'),
]

