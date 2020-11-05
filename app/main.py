from models import User
import form
import platform

tommy = User("debroucker", "tommy", "tommy.debroucker.etu@univ-lille.fr", "31705154")
fname = "./data/courses.csv"
fnameExcel = "./data/courses.xlsx"
test = False
if platform.system == "Windows" :
    fname = "." + fname
    fnameExcel = "." + fnameExcel
form.sendToForm(tommy, fname, fnameExcel, test)