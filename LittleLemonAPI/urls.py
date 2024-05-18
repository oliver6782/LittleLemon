from django.urls import path
from .views import CategoryView, MenuItemView

urlpatterns = [
    path('category/', CategoryView.as_view(), name='category'),
]