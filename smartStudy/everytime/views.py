from django.shortcuts import render, redirect

# Create your views here.
def connect_everytime(request):
    return render(request, 'connect-everytime.html')

def post(request):
    if request.method == "POST":
        print(request.POST.get("user-code"))

        # form = PostForm(request.POST)
        # if form.is_valid():
        #     lotto = form.save(commit = False)
        #     lotto.generate()
        # return redirect('connect-everytime')
        return render(request, 'check-info.html')
    else:
        return render(request, "error.html")

def howto(request):
    return render(request, 'connect-everytime.html')