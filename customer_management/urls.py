# from .views import upload_customer
# from django.urls import path
# from .views import customer_list
# from .views import customer_detail

# urlpatterns = [
#     path('customer_management/upload',upload_customer,name='customer_upload_view'),
#     path("customer_management/list", customer_list, name="customer_list_view"),
#      path("customer_management/<int:id>/",customer_detail,name="customer_detail_view"),  
# ]


from django.urls import path
from . import views
from .views import customer_list
from .views import customer_detail
from .views import upload_customer

urlpatterns = [
    path('customer_management/upload',upload_customer,name='customer_upload_view'),
    path('list/', views.customer_list, name='customer-list'),
    path('customer-detail/<int:id>/', views.customer_detail, name='customer_detail_view'),
    path('edit-detail/<int:id>/', views.edit_customer_view, name='edit_customer_view'),
]
