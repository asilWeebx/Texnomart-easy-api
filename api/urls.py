# urls.py
from django.urls import path
from .views import CardListCreateView, CardRetrieveUpdateDeleteView, CategoryListCreateView

urlpatterns = [
    path('api/categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('api/cards/', CardListCreateView.as_view(), name='card-list-create'),
    path('api/cards/<int:pk>/', CardRetrieveUpdateDeleteView.as_view(), name='card-retrieve-update-delete'),
    path('api/cards/category/<int:category_id>/', CardListCreateView.as_view(), name='card-list-by-category'),
]
