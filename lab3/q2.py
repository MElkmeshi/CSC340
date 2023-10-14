import datetime

class Human:
  def __init__(self,name:str,address:str,dateofbrith:datetime,email:str):
    self._name = name
    self._address = address
    self._dateofbrith = dateofbrith
    self._email = email
    
  def get_name(self) -> str: 
    return self._name 
  def set_name(self, name:str): 
    self._name = name
  def get_address(self) -> str: 
    return self._address 
  def set_address(self, address:str): 
    self._address = address
  def get_email(self) -> str: 
    return self._email 
  def set_email(self, email:str): 
    self._email = email
  def get_dateofbrith(self) -> str: 
    return self.dateofbrith 
  def set_dateofbrith(self, dateofbrith:datetime): 
    self._dateofbrith = dateofbrith

class Student(Human):
    def __init__(self,name:str,address:str,dateofbrith:datetime,email:str, ID: str, GPA: float):
        super().__init__(name, address, dateofbrith, email)
        self._ID = ID
        self._GPA = GPA
    def get_CGPA(totalPointsEarned:int,totalCreditHoursAttempted:int) -> float:
        return totalPointsEarned/totalCreditHoursAttempted

class Lecturer(Human):
    def __init__(self, name: str, address: str, dateofbrith: datetime, email: str,academicRank:str,salary:int,teachingLoad:int):
        super().__init__(name, address, dateofbrith, email)
        self._academicRank = academicRank
        self.salary = salary
        self._courses = []
    def get_bonusSalary(self,extraTeachingHours:int) -> float:
        return extraTeachingHours/8*0.6*self.salary

class Course:
    def __init__(self,code:str,title:str,level:str,lecturer:Lecturer):
        self._code = code
        self._title = title
        self._level = level
        self._lecturer = lecturer
        self._students = []
    def enroll(self,student:Student):
        self._students.append(student)
    def unenroll(self,student:Student):
        self._students.remove(student)
    def assignLecturer(self,lecturer:Lecturer):
        self._lecturer = lecturer
    def get_students(self) -> list[Student]:
        return self._students
    def get_lecturer(self) -> Lecturer:
        return self._lecturer

def main():
    student1 = Student("Mohamed","Libya",datetime.datetime(2002,4,25),"elkmeshi2002@gmail.com","2021/08926",3.1)
    student2 = Student("Ahmed","Egypt",datetime.datetime(2003,6,5),"ahmed2004@gmail.com","2021/08451",3.8)
    lecturer1 = Lecturer("Ashraf","Obour",datetime.datetime(1979,4,1),"astaf@gmail.com","Docrora",80000,15)
    lecturer2 = Lecturer("Wala","Obour",datetime.datetime(1979,4,1),"wala@gmail.com","Docrora",20000,15)
    course1 = Course("SWE546","Network","2nd Year",lecturer1)
    course1.enroll(student1)
    course1.enroll(student2)
    course1.unenroll(student2)
    course1.assignLecturer(lecturer2)
    print(course1.get_students()[0].get_name())
    print(course1.get_lecturer().get_name())

main()