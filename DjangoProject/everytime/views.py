from django.shortcuts import render, redirect
import crawler
from calendarapp.models  import Event
from crawler import Subject
import datetime

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
        # print(info_list)
        

        this_monday = datetime.date(2019, 9, 2)
        while this_monday < datetime.date(2019, 12, 31):
            for i in timetable_list: #과목별
                for j in i.dates: #날자별
                    d = this_monday + datetime.timedelta(days=int(j['day']))

                    hour, min = crawler.calc_time(int(j['start_time']))
                    s = datetime.time(hour, min, 0)

                    hour, min = crawler.calc_time(int(j['end_time']))
                    e = datetime.time(hour, min, 0)

                    start = datetime.datetime.combine(d, s)
                    end = datetime.datetime.combine(d, e)

                    Event(owner=request.user, title=i.name, place=i.place, start=start, end=end, is_from_timetable=True).save()
            this_monday += datetime.timedelta(days=7)


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