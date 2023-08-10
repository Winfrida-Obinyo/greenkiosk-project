

from django.shortcuts import render
from .forms import VendorUploadForm
from inventory.models import Vendor
from django.shortcuts import redirect

# Create your views here.

def upload_vendor(request):                      #the request represents a http request
    if request.method == 'POST':
        uploaded_vendor = request.FILES["image"]
        form = VendorUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = VendorUploadForm()
    return render(request, "vendor/vendor_upload.html", {"form": form})


     
def vendor_list(request):
    vendor = Vendor.objects.all()
    return render (request, "vendor/vendor_list.html", {"vendors":vendor})




def vendor_detail(request,id):
    vendor=Vendor.objects.get(id=id)
    return render(request,"vendor/vendor_detail.html", {"vendor":vendor})




def edit_vendor_view(request,id):
   vendor=Vendor.objects.get(id=id)
   if request.method=='POST':
      form=VendorUploadForm(request.POST,instance=Vendor)
      if form.is_valid():
         form.save()
      return redirect("vendor_edit_view",id=Vendor.id )

   else:
        form=VendorUploadForm(instance=vendor)
   return render (request,"edit/edit_vendor.html",{"form":form})


