from django.urls import path
from .views import upload_order,order_list,order_detail,edit_order_view


urlpatterns = [
    path("order/upload", upload_order, name="order_upload_view"),
    path("order/list", order_list, name="order_list_view"),
    path("order/<int:id>/",order_detail,name="order_detail_view"),  
    path("order/<int:id>/",edit_order_view,name="order_edit_view"), 

    
]



