import sys
import requests
from models import User, Course, COURSES
import datetime

def sendToForm(user:User, test:bool) :
    name = user.name
    fname = user.fname
    mail = user.mail
    nbCard = user.nbCard
    course = getCourse()
    if course == "" :
        print("error : not course actually")
        return 
    courseName = course.name
    if test :
        url = "https://docs.google.com/forms/d/e/1FAIpQLSeTx6CaGAeQPirjCrxzSbuGfixkwtrKZDWikxZgEqI0dixs8w/formResponse"
        d = {
            "emailAddress":mail,
            "entry.1771459457":name,
            "entry.220665083":fname,
            "entry.789303275":nbCard,
            "entry.996298679":courseName,
        }
    else :
        url = "https://docs.google.com/forms/d/e/1FAIpQLSco_brjZ-G9CKnrn9ncxML2dxgKRTkuuVfSoNCPa1WVXAYqwQ/formResponse"
        d = {
            "emailAddress":mail,
            "entry.1179320495":name,
            "entry.1852191993":fname,
            "entry.1448064788":nbCard,
            "entry.677641890":courseName,
        }
    res=requests.post(url, d)
    code = str(res.status_code)
    print("test : " + str(test))
    print("code http response : " + code)
    if code == "200" :
        sout = "submitted with : \n    - mail : " + mail + "\n    - name : " + name + "\n    - first name : " 
        sout += fname + "\n    - number card : " + nbCard + "\n    - course : " + courseName
        if course.linkZoom != "" :
            sout += "\n    - link : " + course.linkZoom
        print(sout)
    else :
        print("error") 
    
def getCourse() : 
    now = datetime.datetime.now()
    courses = COURSES
    weekday = int(now.weekday())
    for c in courses :
        if weekday == c.dayOfWeek and c.begin <= (now + datetime.timedelta(minutes = 10)).time() < c.ending :
            return c 
    return ""