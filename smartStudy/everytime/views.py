from django.shortcuts import render, redirect
import crawler

# Create your views here.
def connect_everytime(request):
    return render(request, 'connect-everytime.html')

def post(request):
    if request.method == "POST":
        user_url = request.POST.get("user-code")
        print("사용자 요청 URL : " + user_url)
        
        timetable_list = crawler.run(user_url)
        if timetable_list == None:
            return render(request, 'error-url.html', {'user_url': user_url})
        info_list = crawler.lecture_list(timetable_list)
        print(info_list)
        
        return render(request, 'check-info.html', {'info_list': info_list})
        # form = PostForm(request.POST)
        # if form.is_valid():
        #     lotto = form.save(commit = False)
        #     lotto.generate()
        # return redirect('connect-everytime')
    else:
        return render(request, "error.html")

def howto(request):
    return render(request, 'connect-everytime.html')