from django.urls import path, include
from rest_framework.routers import DefaultRouter
from todoapp.views import TodoViewSet, UserViewSet

router = DefaultRouter()
router.register(r'todos', TodoViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('todos/<int:pk>/complete/', TodoViewSet.as_view({'post': 'toggle_complete'}), name='toggle_complete'),
    path('', include(router.urls)),
]
