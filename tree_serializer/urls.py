from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_tree, name='get_tree'),
    path("<int:node_pk>/", views.get_subtree, name='get_subtree')
]