# from django.shortcuts import render
# from .forms  import CustomerUploadForm
# from .models import Customer

# # Create your views here.


# def upload_customer(request):                      #the request represents a http request
#     if request.method == 'POST':
#         uploaded_product = request.FILES["image"]
#         form = CustomerUploadForm(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#     else:
#         form = CustomerUploadForm()
#     return render(request, "customer/customer_upload.html", {"form": form})


# def customer_list(request):
#     customers = Customer.objects.all()
#     return render (request, "customer/customer_list.html", {"customer": customers})


# def customer_detail(request,id):
#     customer=Customer.objects.get(id=id)
#     return render(request,"customer/customer_detail.html", {"customer":customer})


from django.shortcuts import render, get_object_or_404,redirect
from .forms import CustomerUploadForm
from .models import Customer

def upload_customer(request):
    if request.method == 'POST':
        form = CustomerUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = CustomerUploadForm()
    return render(request, "customer/customer_upload.html", {"form": form})


def customer_list(request):
    customers = Customer.objects.all()
    return render(request, "customer/customer_list.html", {"customers": customers})


def customer_detail(request, id):
    customer = get_object_or_404(Customer, id=id)
    return render(request, "customer/customer_detail.html", {"customer": customer})



def edit_customer_view(request,id):
   product=Customer.objects.get(id=id)
   if request.method=='POST':
      form=CustomerUploadForm(request.POST,instance=Customer)
      if form.is_valid():
         form.save()
      return redirect("customer_detail_view",id=Customer.id )

   else:
        form=CustomerUploadForm(instance=product)
   return render (request,"customer/edit_customer.html",{"form":form})
     
