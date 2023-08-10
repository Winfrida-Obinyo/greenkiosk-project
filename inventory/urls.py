from django.urls import path
from .views import upload_product,product_list,edit_product_view
from.views import product_detail


urlpatterns = [
    path("product/upload", upload_product, name="product_upload_view"),
    path("product/list", product_list, name="product_list_view"),
    path("product/<int:id>/",product_detail,name="product_detail_view"),  
    path("product/edit/<int:id>/",edit_product_view,name="edit_product_view"),  
    
    
  
]



