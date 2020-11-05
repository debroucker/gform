import sys
import requests
from models import User, Course
import saveData
import datetime

def sendToForm(user:User, filename:str, filenameExcel:str, test:bool) :
    name = user.name
    fname = user.fname
    mail = user.mail
    nbCard = user.nbCard
    course = getCourse()
    courseName = course.name
    if courseName == "" :
        print("error : not course actually")
        return 
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
        print("submitted with : \n    - mail : " + mail + "\n    - name : " + name + "\n    - first name : " 
        + fname + "\n    - number card : " + nbCard + "\n    - course : " + courseName)
        saveData.addInFile(filename, filenameExcel, course)
    else :
        print("error") 

def createCourses() :
    #mercredi
    ang = Course("ANG1 (E. Dewulf)", datetime.time(hour=10, minute=20), 2, 2)
    ro = Course("RO (N. Melab)", datetime.time(hour=14, minute=0), 2, 2)
    icm = Course("ICM (J. Rouillard)", datetime.time(hour=16, minute=0), 2, 2)
    #jeudi
    bda = Course("BDA (F. Bossut)", datetime.time(hour=8, minute=0), 4, 3)
    cp = Course("CP (J. Rakotobe)", datetime.time(hour=14, minute=0), 3, 3)
    #vendredi
    bda = Course("BDA (F. Bossut)", datetime.time(hour=8, minute=0), 4, 3)
    cp = Course("CP (J. Rakotobe)", datetime.time(hour=14, minute=0), 3, 3)
    #vendredi
    c3p = Course("C3P (V. Aranega)", datetime.time(hour=8, minute=0), 4, 4)
    gp = Course("GP (J-Y. Chauvier)", datetime.time(hour=13, minute=30), 3, 4)
    #list
    return [ang, ro, icm, bda, cp, c3p, gp]
    

def getCourse() : 
    now = datetime.datetime.now()
    courses = createCourses()
    weekday = int(now.weekday())
    time = now.time()
    for c in courses :
        if weekday == c.dayOfWeek and c.begin <= time < c.ending :
            return c 
    return ""