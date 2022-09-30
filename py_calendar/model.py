import kender
import kSoundManager as ksm

print(ksm.soundTypes)

class event():

    day = ""
    month = ""
    year = ""
    title = ""
    description = ""

    def __init__(self, day, month, year, title, description):
        self.day = day
        self.month = month
        self.year = year
        self.description = description
        self.title = title

    
