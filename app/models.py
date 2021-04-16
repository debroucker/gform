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


#vendredi
ISI = Course("ISI (N. Agache and co.)", datetime.time(hour=9, minute=00), 3, 4, "")
PAI = Course("PAI (M. Bilasco)", datetime.time(hour=14, minute=00), 3, 4, "https://univ-lille-fr.zoom.us/j/91408041832?pwd=MTA1czJJWnR4V2NpQ3JNRXZreDBRdz09")

COURSES = [ISI, PAI]
