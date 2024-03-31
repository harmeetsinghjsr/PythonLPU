class Student():
  # Construction of parent class
    def _init_(self, name, enrollnumber):
        self.name = name
        self.enrollnumber = enrollnumber
    def display(self):
        print(self.name)
        print(self.enrollnumber)

# child class
class Colleges(Student):
    def _init_(self, name, enrollnumber, admnyear, branch):
        self.name = name
        self.enrollnumber = enrollnumber
        self.admnyear = admnyear
        self.branch = branch

    def display(self):
        print(self.admnyear)
        print(self.branch)
        print(self.enrollnumber)
        print(self.name)

obj = Colleges('rohit',547387,2012,"CSE")
obj.display
