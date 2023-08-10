

# Create your views here.
from django.shortcuts import render
from .forms import ReviewUploadForm
from review.models import Review
from django.shortcuts import redirect


#there are class based views and function based views
# Create your views here.
def upload_review(request):                      #the request represents a http request
    if request.method == 'POST':
        uploaded_review= request.FILES["image"]
        form = ReviewUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = ReviewUploadForm()
    return render(request, "review/review_upload.html", {"form": form})

def review_list(request):
    reviews = Review.objects.all()
    return render (request, "review/review_list.html", {"reviews":reviews})

def review_detail(request,id):
    review=Review.objects.get(id=id)
    return render(request,"review/review_detail.html", {"reviews":review})


def edit_review_view(request,id):
   review=Review.objects.get(id=id)
   if request.method=='POST':
      form=Review(request.POST,instance=Review)
      if form.is_valid():
         form.save()
      return redirect("review_detail_view",id=Review.id )

   else:
        form=ReviewUploadForm(instance=review)
   return render (request,"review/review_edit.html",{"form":form})