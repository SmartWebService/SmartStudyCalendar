import requests
import xml.etree.ElementTree as ET
import json

class Subject:
    def __init__(self, lecture_code, name, professor, place):
        self.lecture_code = lecture_code
        self.name = name
        self.professor = professor
        self.dates = []
        self.place = place

    def __str__(self):
        # return f'{self.lecture_code} {self.name} {self.professor} {self.place} {str(self.dates)}'
        return self.lecture_code + self.name+self.professor+self.place+str(self.dates)

    def add_date(self, day, start_time, end_time):
        date = {'day': day, 'start_time': start_time, 'end_time': end_time}
        self.dates.append(date)


def calc_time(time):
    return time//12, time%12


def timetable2json(timetable):
    json_data = {'events': []}
    for i in timetable:
        # for j in i.dates:
        #     hour, min = calc_time(j.)
        i_sub = {}
        if len(i.lecture_code):
            i_sub['id'] = i.lecture_code
        else:
            i_sub['id'] = i.name
        # i_sub['title'] = f"{i.name} ({i.professor})"
        i_sub['start'] = i
        i_sub['description'] = i.place
        json_data['events'].append(i_sub)
    return json.dumps(json_data)


def lecture_list(_list):
    _result = []

    for i in _list:
        _result.append(i.name)
    
    return _result

def run(user_url):
    _table = []
    # user_url = 'https://everytime.kr/@XZsFeIyLZWJCGXQozIPg'
    if user_url.split('@')[0] != 'https://everytime.kr/':
        return None
        # return ["올바르지 않은 URL입니다.", "요청하신 URL: " + user_url]
    user_code = user_url.split("@")[1]
    print("시간표 고유번호:", user_code)

    xml_url = 'https://everytime.kr/find/timetable/table/friend'

    # Session 생성, with 구문 안에서 유지
    with requests.Session() as s:
        table_req = s.post(xml_url, {'identifier': user_code})

        # 어떤 결과가 나올까요? (200이면 성공!)
        print("HTTP CODE:", table_req.status_code)

        # 로그인이 되지 않으면 경고를 띄워줍시다.
        if table_req.status_code != 200:
            raise Exception('에러!')
    table_data = ET.fromstring(table_req.text)
    print(table_data.findall("./")[0].attrib)

    for i in table_data.findall("./table/subject"):

        lecture_code = i.find('./internal').attrib['value']
        name = i.find('./name').attrib['value']
        professor = i.find('./professor').attrib['value']
        place = i.find('./time/data').attrib['place']
        i_sub = Subject(lecture_code, name, professor, place)

        for j in i.findall('./time/data'):
            i_sub.add_date(j.attrib['day'], j.attrib['starttime'], j.attrib['endtime'])
        _table.append(i_sub)
        print(i_sub)

    # print(timetable2json(_table))
    return _table


if __name__ == '__main__':
    user_url = input("사용자의 에브리타임 시간표 공유 링크를 입력해주세요: ")
    run(user_url)