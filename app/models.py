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