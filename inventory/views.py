from django.shortcuts import render
from .forms import ProductuploadForm


# Create your views here.

# function based views
# request rep a http request   
# render accept request,the template to render the request and data to render the request


def upload_product(request):
    form =ProductuploadForm()
    return render(request,"inventory/product_upload.html",{"form":form})


