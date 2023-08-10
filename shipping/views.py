

# Create your views here.
from django.shortcuts import render
from .forms import ShippingUploadForm
from shipping.models import Shipping
from django.shortcuts import redirect


# Create your views here.

def upload_shipping(request):                      #the request represents a http request
    if request.method == 'POST':
        uploaded_shipping = request.FILES["image"]
        form = ShippingUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = ShippingUploadForm()
    return render(request, "shipping/shipping_upload.html", {"form": form})


def shipping_list(request):
    shippings = Shipping.objects.all()
    return render (request, "shipping/shipping_list.html", {"shippings":shippings})

def shipping_detail(request,id):
    shippings=Shipping.objects.get(id=id)
    return render(request,"shipping/shipping_detail.html", {"shippings":shippings})


def edit_shipping_view(request,id):
   shipping=Shipping.objects.get(id=id)
   if request.method=='POST':
      form=ShippingUploadForm(request.POST,instance=Shipping)
      if form.is_valid():
         form.save()
      return redirect("shipping_edit_view",id=shipping.id )

   else:
        form=ShippingUploadForm(instance=shipping)
   return render (request,"shipping/shipping_detail.html",{"form":form})
     
     