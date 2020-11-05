from models import Course
import datetime
import excel

def addInFile(fname:str, fnameExcel:str, course:Course) :
    res = str(datetime.datetime.now().strftime("%d/%m/%Y-%H:%M")) + "&" + str(course.begin) + "&" + str(course.ending) + "&" + course.name + "&" + str(course.nbHours) +"\n"
    fileToWrite = open(fname, "a")
    fileToWrite.write(res)
    print("saved in DB")
    fileToWrite.close()
    excel.dataToExcel(fname, fnameExcel)