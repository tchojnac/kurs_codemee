class Student:
  min_avg = 4.5
  university = 'New York Academy'

  def __init__(self, name, last, age, student_avg):
    self.name = name
    self.last = last
    self.age = age
    self.student_avg = student_avg


  def __repr__(self):#to samo co __str__
    return self.name.capitalize() + " " + self.last.capitalize()

  def email(self):
    return '{}.{}.university.com'.format(self.name, self.last).lower()
  @property
  def fullname(self):
      return f'{self.name}-{self.last}'
  @fullname.setter
  def fullname(self, newname):
      self.name, self.last = newname.split('-')

#dodac property studentportal account
#nazwa uzytkownika kawalka imienia i wieku
#setter zaktualizowac wiek
#deleter usunie wiek
  @property
  def studentportal(self):
      return f'{self.name}{self.age}'.lower()
  @studentportal.setter
  def studentportal(self, nickname):
      self.name, self.age = nickname.lower()
  @studentportal.deleter
  def studentportal(self):
      self.age = None, None
      print('Dane usuniete!')

obj_anna = Student('Anna', 'Kowalska', 23, 4.4)
obj_arek = Student('Arek', 'Bbb', 23, 4.4)

print(obj_anna.fullname)
obj_anna.fullname = 'Anna-Nowak'

print(obj_anna.fullname)
print(obj_anna.last)
print(obj_anna.email())


print(obj_anna.studentportal)
print(obj_anna.name)
print(obj_anna.age)

