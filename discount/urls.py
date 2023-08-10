from django.urls import path
from.views import discount_detail,discount_list,edit_discount_view,upload_discount



urlpatterns = [
   
    path("discount/<int:id>/",discount_detail,name="discount_detail_view"),  
    path("discount/list",discount_list,name="discount_list_view"),  
    path("discount/<int:id>/",edit_discount_view,name="discount_edit_view"), 
    path("discount/upload",upload_discount,name ="discount_upload_view"),
    
     
    
    
  
]



