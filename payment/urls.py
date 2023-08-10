from django.urls import path
from.views import payment_detail,payment_list,edit_payment_view,upload_payment



urlpatterns = [
   
    path("payment/<int:id>/",payment_detail,name="payment_detail_view"),  
    path("payment/list",payment_list,name="payment_list_view"),  
    path("payment/<int:id>/",edit_payment_view,name="payment_edit_view"), 
    path("payment/upload",upload_payment,name ="payment_upload_view"),
    
     
    
    
  
]



