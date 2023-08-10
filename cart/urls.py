from django.urls import path
from .views import upload_cart, cart_detail, cart_list, edit_cart_view

urlpatterns = [
    path("cart/upload", upload_cart, name="cart_upload_view"),
    path("cart/detail/<int:id>/", cart_detail, name="cart_detail_view"),  # Updated path
    path("cart/list", cart_list, name="cart_list_view"),
    path("cart/edit/<int:id>/", edit_cart_view, name="cart_edit_view"),   # Updated path
]



