class Student:
    def __init__(self, fname, sname, numberOfIndex, average):
        self.firstName = fname
        self.secondName = sname
        self.indexNumber = numberOfIndex
        self.average = average

    def __str__(self) -> str:
        return f"{self.indexNumber} {self.secondName} {self.firstName}, {self.average}"