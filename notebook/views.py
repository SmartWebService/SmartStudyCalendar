from django.shortcuts import render,redirect
from .forms import PostForm
from .models import Post, note
from calendarapp.models  import Event

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

def make_note(request):
    event_id = request.GET['e_id']
    title = Event.objects.get(pk=event_id).title
    if request.method == "GET": # 생성페이지

        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = Post(**form.cleaned_data)
            post.save()
            return redirect('home')
        # return render(request, 'make_note.html', {'title': title})


    if request.method == "POST": # 등록처리
        content = request.POST.get("content")

        note(pk=event_id, e_id=event_id, title=Event.objects.get(pk=event_id).title, content=request.POST.get("content")).save()
        # return render(request, 'make_note.html')
    
    this_note = ""
    if note.objects.filter(pk=event_id):
        this_note = note.objects.filter(pk=event_id)[0].content

    return render(request, 'make_note.html', {'title': title, 'note_content': this_note})
    # else: # 비정상 접근
    #     return redirect('mycalendar')
        