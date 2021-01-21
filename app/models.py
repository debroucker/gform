import datetime

class Course() :
    def __init__(self, name:str, begin:datetime.time, nbHours:int, dayOfWeek:int, linkZoom:str) :
        self.name = name
        self.begin = begin
        self.nbHours = nbHours
        self.ending = (datetime.datetime.combine(datetime.date.today(), begin) + datetime.timedelta(hours=nbHours)).time()
        self.nbHours = nbHours
        self.dayOfWeek = dayOfWeek
        self.linkZoom = linkZoom

class User() :
    def __init__(self, name:str, fname:str, mail:str, nbCard:str) :
        self.name = name.upper()
        self.fname = fname.capitalize()
        self.mail = mail
        self.nbCard = nbCard


#jeudi
CAR = Course("CAR (L. Seinturier)", datetime.time(hour=8, minute=00), 4, 3, "")
ED = Course("ED (L. Jourdan)", datetime.time(hour=13, minute=30), 3, 3, "https://univ-lille-fr.zoom.us/j/92055838734#success")
#vendredi
AFJE = Course("AFJE (F. Secchi)", datetime.time(hour=8, minute=00), 4, 4, "https://univ-lille-fr.zoom.us/j/94277888522#succes")
ANG2 = Course("ANG2 (E. Dewulf)", datetime.time(hour=13, minute=30), 2, 4, "https://univ-lille-fr.zoom.us/j/5614377561#success")
PAI = Course("PAI (M. Bilasco)", datetime.time(hour=16, minute=00), 2, 4, "https://univ-lille-fr.zoom.us/j/91408041832#succes")

COURSES = [CAR, ED, AFJE, ANG2, PAI]