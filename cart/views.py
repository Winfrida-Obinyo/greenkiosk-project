from django.shortcuts import render
from .forms import CartUploadForm
from cart.models import Cart
from django.shortcuts import redirect


# Create your views here.

def upload_cart(request):                      #the request represents a http request
    if request.method == 'POST':
        uploaded_cart = request.FILES["image"]
        form = CartUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = CartUploadForm()
    return render(request, "cart/cart_upload.html", {"form": form})


def cart_list(request):
    carts = Cart.objects.all()
    return render (request, "cart/cart_list.html", {"carts":carts})

def cart_detail(request,id):
    carts=Cart.objects.get(id=id)
    return render(request,"cart/cart_detail.html", {"carts":carts})


def edit_cart_view(request,id):
   cart=Cart.objects.get(id=id)
   if request.method=='POST':
      form=CartUploadForm(request.POST,instance=Cart)
      if form.is_valid():
         form.save()
      return redirect("cart_edit_view",id=cart.id )

   else:
        form=CartUploadForm(instance=cart)
   return render (request,"cart/cart_detail.html",{"form":form})
     
     