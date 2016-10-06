from django.shortcuts import render
from django.http import HttpResponseRedirect
from . forms import ImageUploadForm
from . models import ImageUpload
# Create your views here.

def index(request):
    form = ImageUploadForm
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.image = request.FILES['image']
            post.save()
            return HttpResponseRedirect('/image_upload')
        else:
            form = ImageUploadForm
    return render(request, 'index.html', {'form':form})
 
 
def image_uploaded(request):
    image = ImageUpload.objects.all()
    return render(request, 'image_uploaded.html', {'image':image})