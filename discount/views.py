

# Create your views here.
from django.shortcuts import render
from .forms import DiscountUploadForm
from discount .models import Discount
from django.shortcuts import redirect




# Create your views here.


def upload_discount(request):                      #the request represents a http request
    if request.method == 'POST':
        uploaded_discount = request.FILES["image"]
        form = DiscountUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = DiscountUploadForm()
    return render(request, "discount/discount_upload.html", {"form": form})


def discount_detail(request,id):
    discount=Discount.objects.get(id=id)
    return render(request,"discount/discount_detail.html", {"discount":discount})


def discount_list(request):
    discount = Discount.objects.all()
    return render (request, "discount/discount_list.html", {"discounts":discount})


def edit_discount_view(request,id):
   discount=Discount.objects.get(id=id)
   if request.method=='POST':
      form=DiscountUploadForm(request.POST,instance=discount)
      if form.is_valid():
         form.save()
      return redirect("discount_detail_view",id=discount.id )

   else:
        form=DiscountUploadForm(instance=discount)
   return render (request,"discount/edit_discount.html",{"form":form})
     
     