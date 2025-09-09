from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import (
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    HomeView,
    ContactsView,
    CategoryListView,
    CategoryDetailView,
    CategoryCreateView,
    CategoryUpdateView,
    CategoryDeleteView,
    ProductListFromCategoryView,
)

app_name = CatalogConfig.name

urlpatterns = [
    path("category_list/", CategoryListView.as_view(), name="category_list"),
    path(
        "category_detail/<int:pk>/",
        CategoryDetailView.as_view(),
        name="category_detail",
    ),
    path("category/create/", CategoryCreateView.as_view(), name="category_create"),
    path(
        "category/<int:pk>/update/",
        CategoryUpdateView.as_view(),
        name="category_update",
    ),
    path(
        "category/<int:pk>/delete/",
        CategoryDeleteView.as_view(),
        name="category_confirm_delete",
    ),
    path("", HomeView.as_view(), name="home_view"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("product_list/", ProductListView.as_view(), name="product_list"),
    path(
        "product_detail/<int:pk>/",
        cache_page(60 * 5)(ProductDetailView.as_view()),
        name="product_detail",
    ),
    path("product/create/", ProductCreateView.as_view(), name="product_create"),
    path(
        "product/<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"
    ),
    path(
        "product/<int:pk>/delete/",
        ProductDeleteView.as_view(),
        name="product_confirm_delete",
    ),
    path(
        "product_list/category/<int:category_id>",
        ProductListFromCategoryView.as_view(),
        name="product_list_from_category",
    ),
]
