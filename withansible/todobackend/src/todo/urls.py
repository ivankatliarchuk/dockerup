from  django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from todobackend.src.todo import views

# create a router and register our viewsets with it
router = DefaultRouter(trailing_slash=False)
# Trailing slash = False means Django will expect:
# - http://localhost/todos
# - http://localhost/todos/15

# trailing slash = True means Django will expect:
# - http://localhost/todos/
# - http://localhost/todos/15/
router.register(r'todos', views.TodoItemViewSet)

# The API URLs are now determined automatically by the router
urlpatterns = [
    url(r'^', include(router.urls))
]
