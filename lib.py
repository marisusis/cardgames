class Student(object):
    """docstring for Student."""
    def __init__(self, firstName, lastName):
        super(Student, self).__init__()
        self.firstName = firstName
        self.lastName = lastName
        self.classes = []
    def addClass(self,cls):
        try:
            if (self.classes.count(cls) > 0):
                i=0
                pass
            else:
                self.classes.append(cls)
        except Exception as e:
            raise
        else:
            pass
    def setID(self,id):
        self.id = id
    def printClasses(self):
        i = 0
        result = ""
        classInfos = []
        maxWidth = 0
        while (i < len(self.classes)):
            classInfo = "Block " + int(i + 1) + ": " + self.classes[i].name + " Room: " + int(self.classes[i].room)
            if (len(classInfo) > maxWidth):
                maxWidth = len(classInfo)
            classInfos.append(classInfo)

class Class(object):
    """docstring for Class."""
    def __init__(self, nameClass, room):
        super(Class, self).__init__()
        self.name = name
        self.room = room

def getClasses(student):
    while (True):
        i = 0
