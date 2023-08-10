from django.urls import path
from .views import upload_review,review_list,edit_review_view,review_detail



urlpatterns = [
    path("review/upload", upload_review, name="review_upload_view"),
    path("review/list", review_list, name="review_list_view"),
    path("review/<int:id>/",review_detail,name="review_detail_view"),  
    path("review/edit/<int:id>/",edit_review_view,name="review_edit_view"),  
    
    
  
]



