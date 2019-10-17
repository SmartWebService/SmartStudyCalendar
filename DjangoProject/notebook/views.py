from django.shortcuts import render,redirect
from .forms import PostForm
from .models import Post

# Create your views here.
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = Post(**form.cleaned_data)
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    context = {
        'form' : form
    }
    return render(request, 'post_create.html', context)