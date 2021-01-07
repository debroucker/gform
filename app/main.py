from models import User
import form
import platform

tommy = User("debroucker", "tommy", "tommy.debroucker.etu@univ-lille.fr", "31705154")
test = False
form.sendToForm(tommy, test)