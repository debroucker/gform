from models import User
import form
import platform

tommy = User("debroucker", "tommy", "tommy.debroucker.etu@univ-lille.fr", "31705154")
test = True
if platform.system == "Windows" :
    fname = "." + fname
    fnameExcel = "." + fnameExcel
form.sendToForm(tommy, test)