import datetime

class Course() :
    def __init__(self, name:str, begin:datetime.time, nbHours:int, dayOfWeek:int) :
        self.name = name
        self.begin = begin
        self.nbHours = nbHours
        self.ending = (datetime.datetime.combine(datetime.date.today(), begin) + datetime.timedelta(hours=nbHours)).time()
        self.nbHours = nbHours
        self.dayOfWeek = dayOfWeek

class User() :
    def __init__(self, name:str, fname:str, mail:str, nbCard:str) :
        self.name = name.upper()
        self.fname = fname.capitalize()
        self.mail = mail
        self.nbCard = nbCard


#jeudi
CAR = Course("CAR (L. Seinturier)", datetime.time(hour=8, minute=00), 4, 3)
ED = Course("ED (L. Jourdan)", datetime.time(hour=13, minute=30), 3, 3)
#vendredi
AFJE = Course("AFJE (F. Secchi)", datetime.time(hour=8, minute=00), 4, 4)
ANG2 = Course("ANG2 (E. Dewulf)", datetime.time(hour=13, minute=30), 2, 4)
PAI = Course("PAI (M. Bilasco)", datetime.time(hour=16, minute=00), 2, 4)

COURSES = [CAR, ED, AFJE, ANG2, PAI]