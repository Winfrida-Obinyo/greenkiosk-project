from django.shortcuts import render
from .forms import PaymentUploadForm
from payment .models import Pay
from django.shortcuts import redirect




# Create your views here.


def upload_payment(request):                      #the request represents a http request
    if request.method == 'POST':
        uploaded_product = request.FILES["image"]
        form = PaymentUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = PaymentUploadForm()
    return render(request, "payment/payment_upload.html", {"form": form})


def payment_detail(request,id):
    payment=Pay.objects.get(id=id)
    return render(request,"payment/payment_detail.html", {"payment":payment})

def payment_list(request):
    payment = Pay.objects.all()
    return render (request, "payment/payment_list.html", {"payments":payment})


def edit_payment_view(request,id):
   payment=Pay.objects.get(id=id)
   if request.method=='POST':
      form=PaymentUploadForm(request.POST,instance=payment)
      if form.is_valid():
         form.save()
      return redirect("payment_detail_view",id=payment.id )

   else:
        form=PaymentUploadForm(instance=payment)
   return render (request,"payment/edit_payment.html",{"form":form})
     
     