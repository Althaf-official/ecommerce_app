from django.urls import path

from .views import( 
    product_create_view,
    product_update_view, 
    product_delete_view, 
    product_detail_view,
    product_list_view,
)

urlpatterns = [
    path("products/", product_list_view, name="product-list"),
    path("products/create/", product_create_view, name="product"),
    path("products/<int:id>/", product_detail_view, name='product-detail'),
    path("products/<int:id>/update/", product_update_view, name="product-update"),
    path("products/<int:id>/delete/", product_delete_view, name='product-delete'),
]